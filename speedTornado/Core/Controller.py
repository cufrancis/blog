#!/usr/bin/env Python
# coding=utf-8

import sys, os
sys.path.append("../../")

from speedTornado.config import Config, APP_PATH
from speedTornado.Drivers.Templates import *
import tornado.web

# 控制器父类，所有控制器都应继承此类
class Controller(tornado.web.RequestHandler):
        # super().__init__(self)
        # print("Controller")

    # def initialize(self)
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs) # 执行父类构造方法
        if Config['view']['enable'] == True:
            self.v = eval(Config['view']['engine_name']+'Template')(application, request, **kwargs)

        if os.access(Config['view']['config']['template_dir'], os.W_OK) != True:
            print('View Engine: complie_dir is not writable')
        if os.access(Config['view']['config']['cache_dir'], os.W_OK) != True:
            print('View Engine: cache_dir is not writable')
    #
    #     print(help(self.v))

    def dd(self):
        pass
        # self.render("index")

    # def display(self, tplname = '', **kwargs):
    #     if len(tplname) == 0:
    #         return False
    #     else:
    #         return self.v.render(tplname, **kwargs)

    def display_string(self, chunk):
        # print(help(self.v.write))
        return self.write(chunk)
        # print(self.write(chunk))
        # print(self.v.write(chunk))
