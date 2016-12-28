import sys
sys.path.append("../../../")

from speedTornado.Core.Controller import Controller
from app.model.User import User
import tornado.template as template
# from app.modules.message import messageModule

class BaseController(Controller):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs) # 执行父类构造方法
    #
    # def prepare(self):
    #     print(self.session)


    def get_current_user(self):
        if self.get_secure_cookie('username'):
            username = self.get_secure_cookie('username').decode('utf-8')
        else:
            username = None
        # print(username)
        if username != None:
            user_db = User()
            user = user_db.find(dict(username=username))
            # print(user)
            if user != False:
                self.set_session('user', user)
            else:
                self.set_session('user', '')

            return self.session['user']
        else:
            return None

    # 模板命名空间，自定义函数需要在此引入
    def get_template_namespace(self):
        namespace = dict(
            set_session = self.set_session,
            get_session = self.get_session,
        )
        namespace.update(super().get_template_namespace())
        return namespace
