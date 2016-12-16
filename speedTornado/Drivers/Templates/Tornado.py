
import sys
sys.path.append('../../../')

import tornado.web
from speedTornado.config import Config

# _UNSET = object()

# tornado 自带的模板引擎，此类继承自tornado.template
class TornadoTemplate(tornado.web.RequestHandler):

    # config = {} # 模板配置信息
    pass

    # def __init__(self, application, request, **kwargs):
    #     super(TornadoTemplate, self).__init__(application, request, **kwargs) # 执行父类构造方法
    #
    # def write(self, chunk):
    #     # print(help(tornado.template.Template))
    #     # print(super().write(chunk))
    #     return super().write(chunk)
        # print(help(self))
