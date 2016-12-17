import sys
sys.path.append("../../../")

# from speedTornado.Core.Controller import Controller
from app.controller.BaseHandler import BaseController
from app.model.Article import Article

class index(BaseController):
    def get(self, title):
        article_db = Article()
        article = article_db.find({'slug':title})
        article_db.incrField(article, 'visit', 1)

        self.render('article/show.html', article=article)
