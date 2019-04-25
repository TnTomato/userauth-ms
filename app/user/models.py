#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: ZhangXiaocheng
# @File: models.py
# @Time: 2019/4/15 16:53


from datetime import datetime

from app.ext import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(64))
    salt = db.Column(db.String(20))
    is_enable = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, nullable=True, default=None)

    def __repr__(self):
        return f'<User {self.username}>'
