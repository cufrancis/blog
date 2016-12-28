#!/usr/bin/env Python
# coding=utf-8

import sys, os
sys.path.append("../../")

from speedTornado.config import Config, APP_PATH
from speedTornado.Drivers.Templates import *
import speedTornado.Core.Session as Session
from speedTornado.lib.Debug import dump
from speedTornado.Core.Function import getDt, setDt

import tornado.web

# 控制器父类，所有控制器都应继承此类
class Controller(tornado.web.RequestHandler):

    # def initialize(self)
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs) # 执行父类构造方法
        if Config['view']['enable'] == True:
            self.v = eval(Config['view']['engine_name']+'Template')(application, request, **kwargs)
        # 初始化session
        session_manager = Session.SessionManager(Config["session_secret"], Config["store_options"], Config["session_timeout"])
        self.session = Session.Session(session_manager, self)

        if os.access(Config['view']['config']['template_dir'], os.W_OK) != True:
            print('View Engine: complie_dir is not writable')
        if os.access(Config['view']['config']['cache_dir'], os.W_OK) != True:
            print('View Engine: cache_dir is not writable')

    # 操作成功提示
    def success(self, url, message):
        self.session['message'] = message
        self.session['message_type'] = 2
        self.session.save()
        # self.set_session('message')
        return self.redirect(url)

    # 操作失败提示
    def error(self, url,message):
        self.session['message'] = message
        self.session['message_type'] = 1
        self.session.save()
        return self.redirect(url)

    # name格式，
    # name.subname
    def set_session(self, name, value):
        print("set_session, ", name, value)
        # print(name.split('.'))
        self.session = setDt(name, value, self.session)

    def get_session(self, name):
        try:
            return self.session.get(name)
        except:
            dump("get_session Error...")
