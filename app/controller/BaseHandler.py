import sys
sys.path.append("../../../")

from speedTornado.Core.Controller import Controller
from app.model.User import User

class BaseController(Controller):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs) # 执行父类构造方法

    def get_current_user(self):
        username = self.get_secure_cookie('username').decode('utf-8')
        # print(username)
        if username != None:
            user_db = User()
            user = user_db.find(dict(username=username))
            # print(user)
            if user != False:
                self.session['user'] = ''
                self.session['user'] = user
            else:
                self.session['user'] = ''
                
            return self.session['user']
        else:
            return None
