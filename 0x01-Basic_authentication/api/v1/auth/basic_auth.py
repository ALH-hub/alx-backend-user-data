#!/usr/bin/env python3
"""basic authentication module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """basic authentication class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
        ) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]