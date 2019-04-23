#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: crypto.py
# @Time: 2019/4/18 20:49


import random
from hashlib import sha256


def encrypt(password: str, salt: str=None):
    chars = 'qwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*()_+~'
    if salt:
        the_salt = salt
    else:
        the_salt = ''.join([random.choice(chars) for i in range(16)])
    sha = sha256(the_salt.encode())
    sha.update(password.encode())
    secret = sha.hexdigest()
    return secret, the_salt
