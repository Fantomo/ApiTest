# -*- encoding: utf-8 -*-

from tools.db_tools import db
from order.models import GoodsOrder


def create_order(order_num, goods_id, user_id):

	order = GoodsOrder(order_num=order_num, goods_id=goods_id, user_id=user_id, goods_img=goods_img, stock=stock, category_id=category)

	db.session.add(order)
	db.session.commit()


def search_goods(category, count):
	data = db.session.query(Goods.goods_name, Goods.description, Goods.goods_price, Goods.goods_img, Goods.stock, Goods.category_id)\
	.filter(Goods.category_id == category).filter(Goods.is_del==0).filter(Goods.is_publish==1).filter(Goods.stock > 0)

	return data.all()
