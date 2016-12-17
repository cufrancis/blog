#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
import sys
sys.path.append("./")

# 路由分组
from app.controller.IndexHandler import IndexController
from app.controller.UserHandler import LoginController, RegisterController, LogoutController



# 路由映射表
url = [
    (r'/', IndexController),
    (r'/login', LoginController),
    (r'/register', RegisterController),
    (r'/logout', LogoutController),
]
