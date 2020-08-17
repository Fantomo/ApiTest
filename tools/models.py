# -*- encoding: utf-8 -*-

import sys
sys.path.append("..")
import datetime
from tools.db_tools import db


# 用户表
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

# 商品表
class Goods(db.Model):
	__tabalenmae__ = "goods"

	goods_id = db.Column(db.Integer, primary_key=True)
	goods_name = db.Column(db.String(255), comment="商品名称")
	goods_price = db.Column(db.Numeric(10, 2), comment="商品价格")
	description = db.Column(db.String(255), comment="商品描述")
	is_publish = db.Column(db.Boolean(1), default=1, comment="是否发布 0 未发布 1 发布")
	stock = db.Column(db.Integer, comment="库存")
	is_del = db.Column(db.Boolean(1), default=0, comment="是否删除 0 未删除 1 删除")
	category_id = db.Column(db.Integer, db.ForeignKey("goods_category.id"), comment="商品分类id")
	goods_img = db.Column(db.String(255), comment="商品图片")
	create_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, comment="注册时间")
	update_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False, onupdate=datetime.datetime.now, comment="修改时间")

# 商品分类
class GoodsCategory(db.Model):
	__tabalenmae__ = "goods_category"

	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(32))
	goods = db.relationship("Goods", backref="goodscategory")

# 订单表 
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
