import sys
sys.path.append("../../../")

import tornado.web

# from speedTornado.Core.Controller import Controller
from app.controller.BaseHandler import BaseController
from app.model.Article import Article

article_db = Article()

class index(BaseController):
    def get(self, slug):
        article = article_db.find({'slug':slug})
        article_db.incrField(article, 'visit', 1)

        self.render('article/show.html', article=article)

class edit(BaseController):
    @tornado.web.authenticated
    def get(self, slug):
        article = article_db.find(dict(slug=slug))

        self.set_secure_cookie('message', '')
        self.render('article/edit.html', article=article)

    @tornado.web.authenticated
    def post(self, slug):
        update = dict(
            id = self.get_argument('id'),
            title = self.get_argument('title'),
            slug = self.get_argument('slug'),
            created_at = self.get_argument('created_at'),
            author = self.get_argument('author'),
            content = self.get_argument('content'),
        )
        article = article_db.find(dict(id=update['id']))

        result = article_db.update(dict(id=update['id']), update)

        # print(result)
        if result:
            self.success('/admin/article', '更新成功！')
        else:
            # self.set_secure_cookie('message', "更新失败")
            self.error('/article/edit/{slug}'.format(slug=slug), '更新失败！')
            self.redirect('/admin/article')
