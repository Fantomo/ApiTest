# coding: utf-8

import json, hashlib, time
from flask import request

from tools.db_tools import redis_cli

from . import order
from .db_handle import generate_order, pay_goods, search_user_order


# 商品订单
@order.route("/create_order", methods=['POST'])
def create_order():

	result = {
		"code": "200",
		"msg" :	"请求成功",
		"result": True
	}

	try:
		order = request.json.get("order")
		token = order["token"]

		if not token:
			result['code'] = "403"
			result['msg'] = "请登录账号"
			return json.dumps(result)

		if redis_cli.get_value(token):
			goods_id = order['goods_id']
			user_id = order['uid']
			price = order['price']

			order_num = int(time.time() * 1000)
			status = 1
			generate_order(order_num, goods_id, user_id, status, price)

		else:
			result['code'] = "403"
			result['msg'] = "请检查账号"
			return json.dumps(result)

	except KeyError:
		result['code'] = "400"
		result['msg'] = "请求参数错误"
		return json.dumps(result)

	result['msg'] = "生成订单成功"
	result['order_num'] = order_num

	return result


# 商品订单
@order.route("/pay_order", methods=['POST'])
def pay_order():

	result = {
		"code": "200",
		"msg" :	"请求成功",
		"result": True
	}

	try:
		pay_info = request.json.get("pay")
		token = pay_info["token"]

		if not token:
			result['code'] = "403"
			result['msg'] = "请登录账号"
			return json.dumps(result)

		if redis_cli.get_value(token):
			order_num = pay_info['order_num']
			pay_price = pay_info['pay_price']

			status = 3
			pay_goods(order_num, status, pay_price)

		else:
			result['code'] = "403"
			result['msg'] = "请检查账号"
			return json.dumps(result)

	except KeyError:
		result['code'] = "400"
		result['msg'] = "请求参数错误"
		return json.dumps(result)

	result['msg'] = "支付成功"

	return result


# 获取用户订单信息
@order.route("/get_user_order", methods=['POST'])
def get_user_pay_order():

	result = {
		"code": "200",
		"msg" :	"请求成功",
		"result": True
	}

	try:
		pay_info = request.json.get("user_order")
		token = pay_info["token"]

		if not token:
			result['code'] = "403"
			result['msg'] = "请登录账号"
			return json.dumps(result)

		if redis_cli.get_value(token):
			user_id = pay_info['uid']
			order_status = pay_info['status']

			orders = search_user_order(user_id, order_status)

			o = []

			for order in orders:
				
				order_info = {}
				order_info['order_num'] = order.order_num
				order_info['goods_id'] = order.goods_id
				order_info['order_time'] = str(order.order_time)
				order_info['order_price'] = str(order.order_price)
				order_info['pay_price'] = str(order.pay_price)
				order_info['pay_time'] = order.pay_time

				o.append(order_info)

			result['data'] = o
			return json.dumps(result)


		else:
			result['code'] = "403"
			result['msg'] = "请检查账号"
			return json.dumps(result)

	except KeyError:
		result['code'] = "400"
		result['msg'] = "请求参数错误"
		return json.dumps(result)

	return result
