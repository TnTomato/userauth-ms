#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: config.py
# @Time: 2019/4/15 16:13


import os

DEGBUG_MYSQL_HOST = '127.0.0.1'
DEGBUG_MYSQL_PORT = 3306
DEGBUG_MYSQL_USER = 'root'
DEGBUG_MYSQL_PASSWORD = '123456'
DEGBUG_MYSQL_DB = 'flask_test'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0


class BaseConfig(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    SECRET_KEY = b'_5#y2L"F4Q8z\\n\\xec]/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DEGBUG_MYSQL_USER}:{DEGBUG_MYSQL_PASSWORD}@{DEGBUG_MYSQL_HOST}:{DEGBUG_MYSQL_PORT}/{DEGBUG_MYSQL_DB}'
    CACHE_CONFIG = {
        'CACHE_TYPE': 'redis',
        'CACHE_KEY_PREFIX': 'userms:user_',
        'CACHE_DEFAULT_TIMEOUT': 60,
        'CACHE_REDIS_HOST': REDIS_HOST,
        'CACHE_REDIS_PORT': REDIS_PORT,
        'CACHE_REDIS_DB': REDIS_DB
    }
