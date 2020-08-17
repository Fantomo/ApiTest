# coding:utf-8

import sys
sys.path.append("..")

import datetime
from tools.db_tools import db

class GoodsOrder(db.Model):
	__tabalenmae__ = "goods_order"

	order_id = db.Column(db.Integer, primary_key=True, comment="订单id")
	order_num = db.Column(db.String(129), comment="订单号")
	goods_id = db.Column(db.Integer, comment="商品id")
	user_id = db.Column(db.Integer, comment="购买者id")
	status = db.Column(db.Boolean(1), comment="订单状态：1 待支付；2 已取消；3 已支付")
	order_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, comment="下单时间")
	pay_time = db.Column(db.DateTime, nullable=True, onupdate=datetime.datetime.now, comment="支付时间")
	order_price = db.Column(db.Numeric(10, 2), comment="订单金额")
	pay_price = db.Column(db.Numeric(10, 2), comment="支付金额")
	buyer_remark = db.Column(db.String(255), comment="买家留言")


if __name__ == '__main__':
	db.drop_all()
	db.create_all()
