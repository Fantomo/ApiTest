# -*- encoding: utf-8 -*-

import sys
sys.path.append("..")
import datetime
from tools.db_tools import db


class User(db.Model):
	__tablename__ = "User"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), comment="用户名")
	mobile = db.Column(db.String(20), comment="手机号,登录账号", unique= True)
	password = db.Column(db.String(128))
	email = db.Column(db.String(128), comment="用户邮箱")
	status = db.Column(db.Integer, default=1, comment="用户是否存在 1:存在, 0:不存在")
	create_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, comment="注册时间")
	update_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, onupdate=datetime.datetime.now, comment="修改时间")


if __name__ == '__main__':
	db.drop_all()
	db.create_all()
