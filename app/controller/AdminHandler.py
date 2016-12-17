import sys
sys.path.append("../../../")

import tornado.web
# import tornado.gen

from app.controller.BaseHandler import BaseController

class index(BaseController):
    @tornado.web.authenticated
    def get(self):
        self.write("admin indexs")
