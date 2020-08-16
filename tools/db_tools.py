# -*- encoding: utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tools.config import Config
app = Flask(__name__)

db_config = Config().get('db')

class DBConfig:
	db_host = db_config['host']
	db_port = db_config['port']
	db_user = db_config['user']
	db_passwd = db_config['passwd']
	database = db_config['database']

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (db_user, db_passwd, db_host, db_port, database)

	SQLALCHEMY_POOL_SIZE = 1024

	SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(DBConfig)
db = SQLAlchemy(app)
