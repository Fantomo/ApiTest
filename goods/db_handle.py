# -*- encoding: utf-8 -*-

from tools.db_tools import db
from tools.models import Goods


def add_goods(goods_name, desc, price, goods_img, stock, category):
	goods = Goods(goods_name=goods_name, description=desc, goods_price=price, goods_img=goods_img, stock=stock, category_id=category)

	db.session.add(goods)
	db.session.commit()


def search_goods(category, count):
	data = db.session.query(Goods.goods_id, Goods.goods_name, Goods.description, Goods.goods_price, Goods.goods_img, Goods.stock, Goods.category_id)\
	.filter(Goods.category_id == category).filter(Goods.is_del==0).filter(Goods.is_publish==1).filter(Goods.stock > 0)

	return data.all()


def get_goods_info(goods_id):
	data = db.session.query(Goods.goods_id, Goods.goods_name, Goods.description, Goods.goods_price, Goods.goods_img, Goods.stock, Goods.category_id)\
	.filter(Goods.goods_id == goods_id).filter(Goods.is_del==0).filter(Goods.is_publish==1).filter(Goods.stock > 0)

	return data.all()


def get_goods_all():
	data = db.session.query(Goods.goods_id, Goods.goods_name, Goods.description, Goods.goods_price, Goods.goods_img, Goods.stock, Goods.category_id)\
	.filter(Goods.is_del==0).filter(Goods.is_publish==1).filter(Goods.stock > 0)

	return data.all()
