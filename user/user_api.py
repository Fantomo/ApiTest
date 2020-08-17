# encoding: utf-8

import json, re
import base64, time, hashlib
from flask import request, Response

from . import user
from tools.config import Config
from tools.db_tools import redis_cli
from .db_handle import add_user, query_user


"""
注册接口
"""
@user.route("/signin", methods=['POST'])
def signin():

	result = {
		"code": "200",
		"msg" :	"注册成功",
		"result": True
	}

	try:
		data = request.json.get('signin_data')
		username = data['name']
		password = data['passwd']
		mobile = data['mobile']
		email = data['email']

	except KeyError:
		result['code'] = "400"
		result['msg'] = "请求参数错误"
		return json.dumps(result)

	# 验证手机号
	mobile_pattern = re.compile(r"^1[3-9]\d{9}$")
	if not mobile_pattern.match(mobile):
		result['code'] = "4001"
		result['msg'] = "手机号码格式不正确"
		return json.dumps(result)
	else:
		data = query_user(mobile)
		if data and data.status == 1:
			result['code'] = "4005"
			result['msg'] = "此账号已注册"
			return json.dumps(result)

	# 验证邮箱
	email_pattern = re.compile(r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9]+(\.[a-zA-Z0-9_-]+){0,4}$")
	if not email_pattern.match(email):
		result['code'] = "4002"
		result['msg'] = "邮箱账号格式不正确"
		return json.dumps(result)

	# 验证密码长度
	if len(password) < 6:
		result['code'] = "4003"
		result['msg'] = "密码长度必须大于等于6位"
		return json.dumps(result)

	password = base64.b64encode(password.encode('utf-8'))
	add_user(username, mobile, password, email)
	return json.dumps(result)


"""
登录接口
"""
@user.route("/login", methods=['POST', 'GET'])
def login():

	result = {
		"code": "200",
		"msg" :	"请求成功",
		"result": True
	}

	try:
		data = request.json.get('login_data')
		mobile = data['mobile']
		password = data['password']

	except KeyError:
		result['code'] = "400"
		result['msg'] = "请求参数错误"
		return json.dumps(result)

	mobile_pattern = re.compile(r"^1[3-9]\d{9}$")
	if not mobile_pattern.match(mobile):
		result['code'] = "4001"
		result['msg'] = "手机号码格式不正确"
		return json.dumps(result)

	res = query_user(mobile)
	if res:
		src_passwd = bytes.decode(base64.b64decode(res.password))
		if src_passwd == password:
			# 获取token
			token = set_token(mobile)
			result['msg'] = "登录成功"
			result['uid'] = res.id
			result['token'] = token

			mobile = hashlib.md5(mobile.encode('utf8')).hexdigest()
			redis_cli.r_set(token, mobile, 1800)
			return json.dumps(result), 200, {"set-cookie":"token={}".format(token)}
		else:
			result['code'] = "4002"
			result['msg'] = "手机号或密码错误"
			return json.dumps(result)
	else:
		result['code'] = "4002"
		result['msg'] = "手机号或密码错误"
		return json.dumps(result)

	return json.dumps(result)


# token
def set_token(mobile):
	API_SECRET = "SWDDAGETSAACF"
	encrypt = mobile + str(int(time.time())) + API_SECRET
	return hashlib.md5(encrypt.encode('utf-8')).hexdigest()
