#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
        ) -> str:
        """extract the base64 part of authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if 'Basic ' not in authorization_header:
            return None

        return authorization_header.split("Basic ", 1)[1]