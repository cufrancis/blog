#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
import sys
sys.path.append("./")

from app.controller import *

# from handles import *


# 路由映射表
url = [
    (r'/', IndexController),
]
