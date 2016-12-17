import sys
sys.path.append("../../../")

from speedTornado.Core.Controller import Controller
from app.model.Article import Article

class index(Controller):
    def get(self, title):
        article_db = Article()
        article = article_db.find({'slug':title})

        self.render('article/show.html', article=article)
