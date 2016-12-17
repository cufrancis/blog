import sys
sys.path.append("../../../")

import tornado.web
import tornado.gen
# from speedTornado.config import Config
# from speedTornado.Core.Controller import Controller
import speedTornado.Core.Session as Session

from app.controller.BaseHandler import BaseController
from app.model.User import User

import json

# 用户登录
class login(BaseController):
    def get(self):
        # print(self.get_secure_cookie('username'))
        # print(self.current_user)
        cookieName = self.get_secure_cookie('cookieName')
        self.render('user/login.html', cookieName=cookieName)

    @tornado.gen.coroutine
    def post(self):
        # self.clear_cookie('username')
        username = self.get_argument('username')
        password = self.get_argument('password')

        user_db = User()
        result = user_db.find(dict(username=username, password=password))
        print(result)
        if result == False:
            self.write("登录错误")
        else:
            self.session['user'] = ''
            # self.set_secure_cookie('user', result)
            self.set_secure_cookie('username', username)
            self.set_secure_cookie('cookieName', username)
            self.session['user'] = result
            self.session.save()
            self.write("用户{user}登录成功！\n3秒后跳转到首页".format(user=result['username']))

class register(BaseController):
    def get(self):
        if self.get_secure_cookie('message'):
            message=self.get_secure_cookie('message')
        else:
            message = ''
        self.clear_cookie("message")
        self.render('user/register.html', message=message)

    @tornado.gen.coroutine
    def post(self):
        # self.write("Hello")
        username = self.get_argument('username')
        password = self.get_argument('password')

        user_db = User()

        if len(user_db.findAll(dict(username=username))) != 0:
            self.write("用户名已存在")
        else:
            result = user_db.create(dict(username=username, password=password))

            if result != 0: # Create access
                self.set_secure_cookie('cookieName', username)
                self.write(username+"注册成功，3秒后跳转到登录页面！")
            else:
                self.write("Create Error..")

class logout(BaseController):
    def get(self):
        self.clear_cookie('username')
        self.session['user'] = ''
        self.success("Logout success", '/login')
