# coding: utf-8

from flask import Blueprint

order = Blueprint('order', __name__)

from .order_api import create_order
