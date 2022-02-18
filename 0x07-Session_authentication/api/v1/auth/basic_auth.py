#!/usr/bin/env python3
"""basic auth class template
"""

import binascii
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """inherits from auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extact a base 64
        """
        if (authorization_header is None) or (not isinstance(
                authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode a base 64 auth header
        """
        if (base64_authorization_header is None) or (not isinstance(
                base64_authorization_header, str)):
            return None
        try:
            decodi = base64.standard_b64decode(base64_authorization_header)
            return decodi.decode('utf-8')
        except binascii.Error:
            return None
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """extract user credentiasl"""
        if (decoded_base64_authorization_header is None) or (not isinstance(
                decoded_base64_authorization_header, str)):
            return None, None
        position_index = decoded_base64_authorization_header.find(":")
        if position_index == -1:
            return None, None
        username = decoded_base64_authorization_header[:position_index]
        password = decoded_base64_authorization_header[position_index + 1:]
        return username, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user instace based on email and password
        """
        if (user_email is None) or (not isinstance(user_email, str)):
            return None

        if (user_pwd is None) or (not isinstance(user_pwd, str)):
            return None

        find_user = None
        try:
            find_user = User.search({"email": user_email})
            if (len(find_user) == 0):
                return None

            if (find_user[0].is_valid_password(user_pwd) is False):
                return None
            return find_user[0]
        except KeyError:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets the current user
        """
        auth_header = self.authorization_header(request)

        auth_extract = self.extract_base64_authorization_header(auth_header)

        decode_auth = self.decode_base64_authorization_header(auth_extract)

        user_cred = self.extract_user_credentials(decode_auth)

        user = self.user_object_from_credentials(user_cred[0], user_cred[1])

        return user
