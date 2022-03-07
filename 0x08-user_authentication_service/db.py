#!/usr/bin/env python3
"""DB modulo
"""
from typing import Dict, TypeVar
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError, OperationalError

from user import Base, User


class DB:
    """DB clase
    """

    def __init__(self) -> None:
        """Inicializar una nueva instancia de base de datos
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Objeto de sesión memorizado
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Método que guarda a una usuario en la base de datos
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **args) -> User:
        """Encontrar una usuaria disminuyendo en los keywards
        """
        consult = "SELECT * FROM users "
        i = 0
        for arg, value in args.items():
            if i == 0:
                consult += "WHERE "
            else:
                consult += "AND "
            consult += "{} == '{}'".format(arg, value)
            i += 1
        consult += ";"
        users = None
        try:
            users = self._session.consult(
                User).from_statement(text(consult)).all()
        except OperationalError:
            raise InvalidRequestError
        if len(users) == 0:
            raise NoResultFound
        return users[0]

    def update_user(self, user_id: int, **args) -> None:
        """Actualizar una usuario para su id(
        """
        usr = self.find_user_by(id=user_id)
        for arg, value in args.items():
            if arg not in usr.__dict__.keys():
                raise ValueError
            setattr(usr, arg, value)
            self._session.commit()
