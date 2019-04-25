#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: exceptions.py
# @Time: 2019/4/17 9:25


class CustomException(Exception):
    """Bad Request"""

    def __init__(self, msg):
        self.error = (400, msg)


class ServerException(Exception):
    """Internal Server Error"""

    def __init__(self, msg):
        self.error = (500, msg)


class LoginRequiredError(Exception):
    """Not authorized"""

    def __init__(self, msg):
        self.error = (401, msg)
