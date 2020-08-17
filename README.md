## ApiTest

#### 基于Flask 开发接口, 包括GET, POST, token认证等接口


> #### 配置文件(config.yml), 设置mysql、redis

```
# mysql
db:
  host: 127.0.0.1
  port: 3306
  user: root
  passwd: 2018
  database: flask_api

# redis
redis:
  host: 127.0.0.1
  port: 6379
```

> #### 运行环境: python3、Flask、mysql、redis 

```python
# 导入依赖
pip install -r requirements.txt

# 初始化数据库
python init_db.py

# 运行程序
python main.py
```

## 接口列表
* [注册接口](#signin)
* [登录接口](#login)
* [添加商品](#create_goods)
* [分类商品](#get_goods)
* [商品详情](#goods_info)
* [全部商品](#all_goods)
* [生成订单](#create_order)
* [支付接口](#pay_order)
* [用户订单](#user_order)


> #### <span id="signin">注册接口</span>

```python
请求地址: http://localhost/user/signin
请求方式: POST
请求参数: json格式
{
    "signin_data":{
        "name":"Eric",
        "passwd":"123456",
        "email":"eric@test.com",
        "mobile":"18800000001"
    }
}

返回格式: json格式
{
    "code": "200",
    "msg": "注册成功",
    "result": true
}
```

> #### <span id="login">登录接口</span>

```python
请求地址: http://localhost/user/login
请求方式: POST
请求参数: json格式
{
    "signin_data":{
        "name":"Eric",
        "passwd":"123456",
        "email":"eric@test.com",
        "mobile":"18800000001"
    }
}

返回格式: json格式
{
    "code": "200",
    "msg": "登录成功",
    "result": true,
    "uid": 3,
    "token": "72f063c567e327fc24befe6b011a7f57"
}
```

> #### <span id="create_goods">添加商品接口<span>

```python
请求地址: http://localhost/goods/create_goods
请求方式: POST
请求参数: json格式
{
    "token":"f90ccef78c80ece12f5cd43c1571d504",
    "goods_info": {
        "goods_name": "小米电视5 65英寸",
        "price": "3999",
        "description": "4K广色域屏幕 画质细腻若真/时尚全面屏设计/金属机身 尽显简约之美/支持8K视频内容/杜比震撼音效/支持远场语音 一呼即应/3GB+32GB大存储/海量好内容",
        "stock": "200",
        "category": "3",
        "goods_img":"https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296"
    }
}

返回格式: json格式
{
  "code": "200",
  "msg": "添加成功",
  "result": true
}
```

> #### <span id="get_goods">获取分类商品<span>

```python
请求地址: http://localhost/goods/get_goods
请求方式: GET
请求参数: 
    category=1 # 商品分类
    token=a28def36b803b5cfd60c4a13598e8962
    count=5 # 没用

返回格式: json格式
{
    "code": "200",
    "msg": "查询成功",
    "result": true,
    "data": [
        {
            "id": 4,
            "goods_name": "小米电视",
            "description": "智能电视",
            "price": "1999.00",
            "goods_img": "https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296",
            "category_id": 3
        },
        {
            "id": 5,
            "goods_name": "小米电视5 65英寸",
            "description": "4K广色域屏幕 画质细腻若真/时尚全面屏设计/金属机身 尽显简约之美/支持8K视频内容/杜比震撼音效/支持远场语音 一呼即应/3GB+32GB大存储/海量好内容",
            "price": "3999.00",
            "goods_img": "https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296",
            "category_id": 3
        }
    ]
}
```

> #### <span id="goods_info">获取商品详情<span>

```python
请求地址: http://localhost/goods/goods_info
请求方式: GET
请求参数: 
    goods_id=1 # 商品id
    token=f90ccef78c80ece12f5cd43c1571d504

返回格式: json格式
{
    "code": "200",
    "msg": "查询成功",
    "result": true,
    "data": {
        "id": 5,
        "goods_name": "小米电视5 65英寸",
        "description": "4K广色域屏幕 画质细腻若真/时尚全面屏设计/金属机身 尽显简约之美/支持8K视频内容/杜比震撼音效/支持远场语音 一呼即应/3GB+32GB大存储/海量好内容",
        "price": "3999.00",
        "goods_img": "https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296",
        "stock": 200
    }
}
```

> #### <span id="all_goods">获取全部商品<span>

```python
请求地址: /goods/all_goods
请求方式: GET
请求参数: 
    token=f90ccef78c80ece12f5cd43c1571d504

返回格式: json格式
{
    "code": "200",
    "msg": "查询成功",
    "result": true,
    "data": [
        {
            "id": 2,
            "goods_name": "iphone",
            "description": "智能手机",
            "price": "5999.00",
            "goods_img":"https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296",
            "category_id": 1
        },
        {
            "id": 5,
            "goods_name": "小米电视5 65英寸",
            "description": "4K广色域屏幕 画质细腻若真/时尚全面屏设计/金属机身 尽显简约之美/支持8K视频内容/杜比震撼音效/支持远场语音 一呼即应/3GB+32GB大存储/海量好内容",
            "price": "3999.00",
            "goods_img": "https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1572837360.5573296",
            "category_id": 3
        }
    ]
}
```

> #### <span id="create_order">生成订单<span>

```python
请求地址: http://localhost/order/create_order
请求方式: POST
请求参数: json格式
{
    "order": {
        "goods_id": 2,
        "uid": 1,
        "price": "500",
        "token": "c736e4f1dcf0d9074b1f5a7bfeb7bf73"
    }
}

返回格式: json格式
{
  "code": "200",
  "msg": "生成订单成功",
  "order_num": 1597669836482,
  "result": true
}
```

> #### <span id="pay_order">支付接口<span>

```python
请求地址: http://localhost/order/pay_order
请求方式: POST
请求参数: json格式
{
    "pay": {
        "order_num": "1597669797663", # 订单号
        "pay_price": "500",
        "token": "6b0baa9079df1e660fe97bab5434f631"
    }
}

返回格式: json格式
{
  "code": "200",
  "msg": "支付成功",
  "result": true
}
```

> #### <span id="user_order">获取用户订单<span>

```python
请求地址: http://localhost//order/get_user_order
请求方式: POST
请求参数: json格式
{
    "user_order": {
        "uid": "1", # 用户id
        "status": "1", # 订单状态
        "token": "72f063c567e327fc24befe6b011a7f57"
    }
}

返回格式: json格式
{
    "code": "200",
    "msg": "请求成功",
    "result": true,
    "data": [
        {
            "order_num": "1597669513971",
            "goods_id": 2,
            "order_time": "2020-08-17 21:05:14",
            "order_price": "500.00",
            "pay_price": "None",
            "pay_time": null
        },
        {
            "order_num": "1597669836482",
            "goods_id": 2,
            "order_time": "2020-08-17 21:10:37",
            "order_price": "500.00",
            "pay_price": "None",
            "pay_time": null
        }
    ]
}
```
