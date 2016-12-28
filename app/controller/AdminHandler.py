import sys
sys.path.append("../../../")

import tornado.web
# import tornado.gen

from app.controller.BaseHandler import BaseController
from app.model.Article import Article

class index(BaseController):
    @tornado.web.authenticated
    def get(self):
        self.render("admin/index.html")

class article(BaseController):
    @tornado.web.authenticated
    def get(self):
        article_db = Article()
        articles = article_db.findAll()
        self.render('admin/article.html', articles=articles)
