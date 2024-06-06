#!/usr/bin/env python3
"""authentication module"""
from flask import request
from typing import List, TypeVar
import re
import os


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        for p in excluded_paths:
            if p[-1] == '*' and re.match(p[:-1], path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """header authorization function"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current user method"""
        pass

    def session_cookie(self, request=None):
        """session cookie method"""
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
