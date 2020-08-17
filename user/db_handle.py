# -*- encoding: utf-8 -*-

from tools.db_tools import db
from tools.models import User


def add_user(user, mobile, passwd, email):
	user = User(username=user, mobile=mobile, password=passwd, email=email)
	db.session.add(user)
	db.session.commit()


def query_user(mobile):
	return User.query.filter_by(mobile=mobile).first()
