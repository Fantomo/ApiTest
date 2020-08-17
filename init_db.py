# -*- encoding: utf-8 -*-

from tools.db_tools import db
from tools.models import *

if __name__ == '__main__':
	db.drop_all()
	db.create_all()