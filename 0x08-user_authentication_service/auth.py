#!/usr/bin/env python3
"""hash una contraseña"""

from typing import Union
import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


class Auth:
    """Clase de autenticación para interactuar con la base de datos de autenticación..
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Devuelve la usuario registrada
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pwd = _hash_password(password)
            return self._db.add_user(email, pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """validar la contraseña
        """
        try:
            usr = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  usr.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """crea un id de sesión crea una sesión
        """
        try:
            usr = self._db.find_user_by(email=email)
            self._db.update_user(usr.id, session_id=_generate_uuid())
            return usr.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ devuelve el Usuario correspondiente o Ninguno por su id
        """
        if session_id is None:
            return None
        try:
            usr = self._db.find_user_by(session_id=session_id)
            return usr
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destruir la sesión de un usuario
        """
        self._db.update_user(user_id=user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """descansar una contraseña por su correo electrónico
        """
        try:
            usr = self._db.find_user_by(email=email)
            rest_tok = _generate_uuid()
            self._db.update_user(usr.id, reset_token=rest_tok)
            return rest_tok
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ actualiza la contraseña
        """
        try:
            usr = self._db.find_user_by(reset_token=reset_token)
            new_p = _hash_password(password)
            self._db.update_user(usr.id, hashed_password=new_p)
            self._db.update_user(usr.id, reset_token=None)
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """contraseña"""
    hash_p = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash_p


def _generate_uuid() -> str:
    """devuelve una cadena en uuid
    """
    return str(uuid.uuid4())
