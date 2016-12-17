#!/usr/bin/env Python
# coding=utf-8

import sys, os
sys.path.append("../../")

from speedTornado.config import Config, APP_PATH
from speedTornado.Drivers.Templates import *
import speedTornado.Core.Session as Session
import tornado.web

# 控制器父类，所有控制器都应继承此类
class Controller(tornado.web.RequestHandler):

    # def initialize(self)
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs) # 执行父类构造方法
        if Config['view']['enable'] == True:
            self.v = eval(Config['view']['engine_name']+'Template')(application, request, **kwargs)
        session_manager = Session.SessionManager(Config["session_secret"], Config["store_options"], Config["session_timeout"])
        self.session = Session.Session(session_manager, self)

        if os.access(Config['view']['config']['template_dir'], os.W_OK) != True:
            print('View Engine: complie_dir is not writable')
        if os.access(Config['view']['config']['cache_dir'], os.W_OK) != True:
            print('View Engine: cache_dir is not writable')


        # return self.session['user']
        # return self.get_secure_cookie("username")

    # # 模板命名空间，自定义函数需要在此引入
    def get_template_namespace(self):
        namespace = dict(
            # user = self.get_user
        )
        namespace.update(super().get_template_namespace())
        return namespace
    #
    # # 返回当前用户
    # def get_user(self):
    #     return self.session['user']

    # 成功弹窗提示
    def success(self, msg, url):
        url = "window.history.back()" if len(url) == 0 else "location.href=\"{url}\";".format(url=url)
        self.write('<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><script>function sptips(){alert(\"'+msg+'");'+url+'}</script></head><body onload=\"sptips()\"></body></html>')
