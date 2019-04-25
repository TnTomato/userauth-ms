#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: token.py
# @Time: 2019/4/18 20:46

import base64
import json
import uuid
from datetime import datetime

from app.user.models import User
from app.utils.crypto import encrypt


class Token(object):
    _header = {
        'typ': 'JWT',
        'alg': 'HS256'
    }
    _payload = {
        'iss': 'Aegis',  # Issuer
        'exp': 7200,  # Expiration time
        'sub': 'Authorization',  # Subject
        'aud': 'Aegis-User',  # Audience
    }
    _secret = 'ec#j0$n%xv3w_(ca'


class TokenGenerator(Token):

    def __init__(self, user_obj: User):
        self.header = self._header
        self.payload = self._payload
        self.secret = self._secret
        self.payload.update({
            'iat': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Issued at
            'jti': str(uuid.uuid1()),  # JWT id
            'username': user_obj.username
        })

    def __str__(self):
        return self._generate()

    def _generate(self):
        h = base64.urlsafe_b64encode(json.dumps(self.header).encode()).decode()
        p = base64.urlsafe_b64encode(json.dumps(self.payload).encode()).decode()
        s = encrypt('.'.join([h, p]), self.secret)[0]
        return '.'.join([h, p, s])


class TokenParser(Token):

    @staticmethod
    def get_payload(token):
        payload_part = token.split('.')[1]
        payload = json.loads(base64.urlsafe_b64decode(payload_part))
        return payload


class TokenValidator(Token):

    @staticmethod
    def validate_token(token):
        now = datetime.now()
        encoded_payload = token.split('.')[1]
        payload = json.loads(base64.urlsafe_b64decode(encoded_payload))
        iat = datetime.strptime(payload['iat'], '%Y-%m-%d %H:%M:%S')
        expiration = payload['exp']
        delta = (now - iat).seconds
        return True, payload if delta <= expiration else False, None
