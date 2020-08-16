# coding: utf-8

from flask import Blueprint

user = Blueprint('user', __name__)

from .user_api import signin, login
