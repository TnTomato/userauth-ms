#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: decorators.py
# @Time: 2019/4/17 9:18


import traceback

from flask import jsonify, request

from app.exceptions import CustomException, ServerException, LoginRequiredError
from app.ext import cache
from app.utils.token import TokenParser


def set_response(code: int=200, msg: str='ok', data=None) -> dict:
    if not data:
        data = []
    return {
        'code': code,
        'data': data,
        'msg': msg
    }


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomException as err:
            code = err.error[0]
            msg = err.error[1]
            return jsonify(set_response(code, msg))
        except ServerException as err:
            code = err.error[0]
            msg = err.error[1]
            return jsonify(set_response(code, msg))
        except LoginRequiredError as err:
            code = err.error[0]
            msg = err.error[1]
            return jsonify(set_response(code, msg))
        except Exception as err:
            msg = traceback.format_exc()
            return jsonify(set_response(500, msg))

    return wrapper


def token_validator(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('X-Token')
        if not token:
            raise LoginRequiredError('Login required')
        else:
            payload = TokenParser.get_payload(token)
            username = payload['username']
            cached_token = cache.get(f'token_{username}')
            if cached_token:
                cache.set(f'token_{username}', token)
            else:
                raise LoginRequiredError('Invalid token')
        return func(*args, **kwargs)

    return wrapper
