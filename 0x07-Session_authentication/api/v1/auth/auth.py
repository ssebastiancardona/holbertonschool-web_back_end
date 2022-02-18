#!/usr/bin/env python3
"""
manejar la autenticación con una clase
"""

from os import getenv
from typing import List, TypeVar
from flask import request


class Auth():
    """una clase para comprobar la autenticación básica de las rutas
    """

    def require_auth(self, path: str, excluded_paths:
        List[str]) -> bool:
        """si la ruta necesita autenticación
        """
        if (path is None) or (excluded_paths is None or
                              len(excluded_paths) == 0):
            return True

        if path[-1] == '/':
            if path in excluded_paths:
                return False
            return True

        path_sl = path + '/'
        if path_sl in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """compruebe si el encabezado recibe la autenticación
        """
        if (request is None):
            return None

        if "Authorization" not in request.headers.keys():
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Devuelve la usuario de registro actual
        """
        return None

    def session_cookie(self, request=None):
        """devuelve el valor de la cookie en función de la solicitud
        """
        if request is None:
            return None

        id_sesion = getenv("SESSION_NAME")
        galleta = request.cookies.get(id_sesion)
        return galleta
