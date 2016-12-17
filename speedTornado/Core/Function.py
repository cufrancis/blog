
import sys, os
sys.path.append("../../")

import json
import re

# 替换函数，将
def stReplace(pattern, repl, string):
    return re.sub((pattern), repl, string)
    # pass

# 字符串转换成字典
def strToDict(string):
    return json.loads(string)
