import sys
sys.path.append('../../')
# sys.path.append('../Drivers/')# 增加驱动搜索目录

from speedTornado.config import Config
from speedTornado.Core.Model import Model

class User(Model):

    tbl_name = 'users'


    def __init__(self):
        super(User, self).__init__()

    # def find(self, conditions = {}, sort = '', fields = ''):
    #     return super().__init__(conditions, sort, fields, tpl_name)
