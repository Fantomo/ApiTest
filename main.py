# coding: utf-8

from flask import Flask
from user.user_api import signin, login
from goods.goods_api import create_goods, get_goods
from user import user
from goods import goods
from order import order

app = Flask(__name__)

app.route("/signin")(signin)
app.route("/login")(login)
app.route("/create_goods")(create_goods)
app.route("/get_goods")(get_goods)


app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(goods, url_prefix="/goods")
app.register_blueprint(order, url_prefix="/order")


if __name__ == '__main__':
	app.run("0.0.0.0", port="80", debug=True)
