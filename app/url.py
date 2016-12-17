#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
import sys
sys.path.append("./")

# 路由分组
import app.controller.IndexHandler as Index
import app.controller.UserHandler as User
import app.controller.ArticleHandler as Article
import app.controller.AdminHandler as Admin



# 路由映射表
url = [
    (r'/', Index.index),
    (r'/login', User.login),
    (r'/register', User.register),
    (r'/logout', User.logout),

    (r'/article/(.*)', Article.index),
    (r'/admin', Admin.index)
]
