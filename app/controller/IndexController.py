import sys
sys.path.append("../../../")

# print(sys.path)
import tornado.web
# from speedTornado.config import Config
from speedTornado.Core.Controller import Controller
from app.model.User import User

class IndexController(Controller):
    def get(self):
        user = User()
        # print(user.tpl_name)
        result = user.find({'username':'cufrancis'})
        # print(user.dumpSql())
        # print(result[0]['username'])
        # self.write(result[0]['username'])
        self.render('index.html', user=result[0])
