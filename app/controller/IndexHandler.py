import sys
sys.path.append("../../../")

# print(sys.path)
import tornado.web
# from speedTornado.config import Config
# from speedTornado.Core.Controller import Controller
from speedTornado.Core.Function import strToDict, stReplace

from app.controller.BaseHandler import BaseController
from app.model.User import User
from app.model.Article import Article
# import app.model.Article as Article
from speedTornado.lib.baiduTranslate import baiduTranslate

class index(BaseController):
    def get(self):
        article_db = Article()
        articles = article_db.findAll()

        # self.set_session("user")
        # self.get_session('user')

        # 新增文章时使用，查询sulg
        # ss = baiduTranslate()
        # print(stReplace(' ', '-', ss.translate("我爱你 宝贝", 'zh', 'en')))
        self.render('index.html', articles=articles)
