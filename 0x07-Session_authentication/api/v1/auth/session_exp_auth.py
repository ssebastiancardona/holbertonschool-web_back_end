#!/usr/bin/env python3
"""fecha de caducidad
"""


from datetime import datetime, timedelta
from os import getenv
from api.v1.auth.session_auth import SessionAut


class SessionExpAuth(SessionAut):
    """agregando una fecha de caducidad a la autenticación de sesión
    """

    def __init__(self) -> None:
        """inicializa la clase
        """
        super().__init__()
        try:
            self.session_duration = int(getenv("SESSION_DURATION", default=0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ID de sesión
        """
        new_session = super().create_session(user_id)
        if new_session is None:
            return None

        self.user_id_by_session_id[new_session] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return new_session

    def user_id_for_session_id(self, session_id=None):
        """obtiene la identificación del usuario si todavía hay tiempo
        """
        if session_id is None:
            return None

        if (session_id not in self.user_id_by_session_id):
            return None

        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id]["user_id"]

        session_dict = self.user_id_by_session_id[session_id]
        if "created_at" not in session_dict:
            return None

        if (session_dict["created_at"] +
                timedelta(seconds=self.session_duration) < datetime.now()):
            return None

        return session_dict["user_id"]
