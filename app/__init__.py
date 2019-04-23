#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: __init__.py
# @Time: 2019/4/15 11:26


from flask import Flask

from app.ext import db, cache


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DebugConfig')

    db.init_app(app)
    cache.init_app(app, config=app.config['CACHE_CONFIG'])

    from app.user.views import user_bp
    app.register_blueprint(user_bp)

    return app
