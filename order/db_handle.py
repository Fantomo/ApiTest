# -*- encoding: utf-8 -*-

from tools.db_tools import db
from tools.models import GoodsOrder


def generate_order(order_num, goods_id, user_id, status, order_price):

	order = GoodsOrder(order_num=order_num, goods_id=goods_id, user_id=user_id, status=status, order_price=order_price)

	db.session.add(order)
	db.session.commit()


def pay_goods(order_num, status, pay_price):
	GoodsOrder.query.filter_by(order_num=order_num).update({"status": status, "pay_price": pay_price})
	db.session.commit()


def search_user_order(uid, status):
	return GoodsOrder.query.filter_by(user_id=uid).filter_by(status=status).all()
