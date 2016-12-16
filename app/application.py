#!/usr/bin/env Python
# coding=utf-8

from app.url import url

import tornado.web
import os
# from handles.error import ErrorHandler

settings = dict(
    # 调试模式
    debug = False,

    # 默认的错误处理函数
    # default_handler_class = ErrorHandler,
    # default_handler_args = dict(status_code = 404),

    # 自动压缩文本格式的响应数据
    compress_response = True,

    serve_traceback = True,

    # 控制对模板的自动转义
    autoescape = None,
    # 控制模板是否在每次请求时重新编译，默认True
    compiled_template_cache = True,
    # 模板所在文件夹
    template_path = os.path.join(os.path.dirname(__file__), "view"),

    # 静态文件所在文件夹
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    static_url_prefix = '/static/',

    # 认证和安全设置
    # cookie加密密文
    cookie_secret = "AdVhPUvrSpymMgsYuExPb63NAvW1zk0IqomnQJxtocU=",
    # 开启XSRF防护
    xsrf_cookies = True,
    # 如果用户没有登录，authenticated 装饰器会重定向到此url
    login_url = '/',

)

application = tornado.web.Application(
    handlers = url,
    **settings
)
