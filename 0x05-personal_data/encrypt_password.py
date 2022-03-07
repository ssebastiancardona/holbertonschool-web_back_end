#!/usr/bin/env python3
""" Cifrado de contraseñas """
import bcrypt


def hash_password(password: str) -> bytes:
    """ espera una contraseña de nombre de argumento de cadena y devuelve un salted,
        contraseña hash, que es una cadena de bytes. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ espera 2 argumentos y devuelve un valor booleano. """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
