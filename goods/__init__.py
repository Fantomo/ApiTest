# coding: utf-8

from flask import Blueprint

goods = Blueprint('goods', __name__)

from .goods_api import create_goods
