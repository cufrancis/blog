#!/usr/bin/env Python
# coding=utf-8

import os
APP_PATH = os.getcwd() # 项目根目录

# print(APP_PATH)

Config = dict(
    debug=True, # 调试模式，输出执行sql，执行时间
    st_drivers_path = os.path.abspath(os.curdir) + '/Core', # 框架MVC核心目录
    view_registered_functions = [], # 视图内注册的函数记录
    st_app_id = '', # 框架标识id

    db = dict(
        driver = 'mysql',
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '00000000',
        database = 'game',
        prefix = '',
        charset = 'utf8',
    ),
    db_driver_path = '',
    view = dict(
        enable = True, # 开启视图
        config = dict(
			template_dir = APP_PATH + '/app/view/view', # 模板目录
			compile_dir = APP_PATH + '/tmp', # 编译目录
			cache_dir = APP_PATH + '/tmp', # 缓存目录
			left_delimiter = '{',  # smarty左限定符
			right_delimiter = '}', # smarty右限定符
			auto_literal = True, # Smarty3新特性
        ),
        engine_name = 'Tornado'
    ),
    baiduTranslate = dict(
        appid = '20151113000005349',
        secretKey = 'osubCEzlGjzvw8qdQc41',
    ),

    session_secret = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
    session_timeout = 60,# session 超时时间，单位秒
    store_options = {
        'redis_host': 'localhost',
        'redis_port': 6379,
        'redis_pass': '',
    },


)
