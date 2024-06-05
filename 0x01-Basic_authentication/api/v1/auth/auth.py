#!/usr/bin/env python3
"""authentication module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication method"""
        pass

    def authorization_header(self, request=None) -> str:
        """header authorization function"""
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """current user method"""
        pass
