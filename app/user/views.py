#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: views.py
# @Time: 2019/4/15 16:47


from flask import Blueprint, jsonify, request

from app.exceptions import CustomException
from app.ext import db, cache
from app.user.models import User
from app.utils.crypto import encrypt
from app.utils.restful import RESTfulView, LoginRequiredView
from app.utils.token import TokenGenerator

user_bp = Blueprint('user', __name__, template_folder='templates')


class UserRegister(RESTfulView):

    def post(self):
        result = self.init_response()
        username = request.form['username']
        password = request.form['password']
        encrypted, salt = encrypt(password)
        user = User(username=username,
                    password=encrypted,
                    salt=salt)
        db.session.add(user)
        db.session.commit()
        return jsonify(result)


class UserLogin(RESTfulView):

    def post(self):
        result = self.init_response()
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            raise CustomException('Invalid username')
        salt = user.salt
        secret = user.password
        if encrypt(password, salt)[0] == secret:
            token = str(TokenGenerator(user))
            cache.set(f'token_{username}', token)
            result['data'] = {
                'username': username,
                'access_token': token
            }
        else:
            raise CustomException('Invalid password')
        return jsonify(result)


class Test(LoginRequiredView):

    def get(self):
        result = self.init_response()
        token = cache.get('token_eathon')
        result['data'] = token
        return jsonify(result)


user_bp.add_url_rule('/v1/user/register',
                     view_func=UserRegister.as_view('register_view'))
user_bp.add_url_rule('/v1/user/login',
                     view_func=UserLogin.as_view('login_view'))
user_bp.add_url_rule('/test', view_func=Test.as_view('test'))
