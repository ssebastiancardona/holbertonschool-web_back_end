#!/usr/bin/env python3
"""hacer una clase de autenticación de sesión
"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAut(Auth):
    """clase a nueva sesión de autenticación
    """

    user_id_by_sesion_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """crea la identificación
        de la sesión
        """
        if (user_id is None) or (not isinstance(user_id, str)):
            return None

        n_id = str(uuid.uuid4())
        self.user_id_by_sesion_id[n_id] = user_id
        return n_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """devuelve las bases de identificación de usuario en la sesión
        """
        if (session_id is None) or (not isinstance(session_id, str)):
            return None

        user_ = self.user_id_by_sesion_id.get(session_id)
        return user_

    def current_user(self, request=None):
        """basado en el valor de la cookie
        """
        cookie_value = self.session_cookie(request)
        us_id = self.user_id_for_session_id(cookie_value)
        user_ = User.get(us_id)
        return user_

    def destroy_session(self, request=None):
        """destruye la sesión
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)
        if cookie is None:
            return False

        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return False

        del self.user_id_by_sesion_id[cookie]
        return True
