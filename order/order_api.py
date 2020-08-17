# coding: utf-8

import json, hashlib
from flask import request

from tools.db_tools import redis_cli

from . import order
# from .db_handle import add_goods, search_goods

"""
	添加商品接口
"""
@order.route("/create_order", methods=['POST'])
def create_order():
	pass

	# result = {
	# 	"code": "200",
	# 	"msg" :	"请求成功",
	# 	"result": True
	# }
	# try:
	# 	token = request.json.get("token")

	# 	if not token:
	# 		result['code'] = "403"
	# 		result['msg'] = "请登录账号"
	# 		return json.dumps(result)

	# 	if redis_cli.get_value(token):
	# 		data = request.json.get('goods_id')
	# 		goods_name = data['goods_name']
	# 		description = data['description']
	# 		price = data['price']
	# 		stock = data['stock']
	# 		category = data['category']
	# 		goods_img = data['goods_img']
	# 	else:
	# 		result['code'] = "403"
	# 		result['msg'] = "请检查账号"
	# 		return json.dumps(result)

	# except KeyError:
	# 	result['code'] = "400"
	# 	result['msg'] = "请求参数错误"
	# 	return json.dumps(result)

	# add_goods(goods_name, description, price, goods_img, stock, category)
	# result['msg'] = "添加成功"

	# return result
