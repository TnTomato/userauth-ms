#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: restful.py
# @Time: 2019/4/18 20:48


from flask import views

from app.decorators import set_response, exception_handler, token_validator


class RESTfulView(views.MethodView):

    decorators = [exception_handler]

    @classmethod
    def init_response(cls, code: int=200, msg: str='ok', data=None):
        return set_response(code, msg, data)


class LoginRequiredView(RESTfulView):

    decorators = [token_validator, exception_handler]
