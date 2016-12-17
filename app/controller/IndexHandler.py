import sys
sys.path.append("../../../")

# print(sys.path)
import tornado.web
# from speedTornado.config import Config
from speedTornado.Core.Controller import Controller
from app.model.User import User
from app.model.Article import Article
# import app.model.Article as Article

class IndexController(Controller):
    def get(self):
        article_db = Article()
        articles = article_db.findAll()

        # print(self.current_user)

        self.render('index.html', articles=articles)
