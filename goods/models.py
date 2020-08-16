# coding:utf-8

import sys
sys.path.append("..")

import datetime
from tools.db_tools import db

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


class GoodsCategory(db.Model):
	__tabalenmae__ = "goods_category"

	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(32))
	goods = db.relationship("Goods", backref="goodscategory")	


if __name__ == '__main__':
	db.drop_all()
	db.create_all()
