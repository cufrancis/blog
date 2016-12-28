
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

# 使用study.name形式设置字典值
def setDt(name, value, dt):
    """ Use the Period symbol in Python to set the value of the dictionary
    Args:
        name: to set the key name, support nesting
    """
    tmp = name.split('.')
    num = len(tmp)
    vals = dt
    for k in tmp:
        if k in dt:
            if isinstance(vals, dict) == True:
                vals = dt.get(k)
            else:
                vals[k] = value
                vals = dt.get(k)
        elif k in vals:
            vals[k] = value
        else:
            num = num -1
            if num != 0:
                vals[k] = dict()
                vals = vals.get(k)
            else:
                vals[k] = value
    return dt

# 成功返回指定键值，失败返回None
def getDt(name, dt):
    # 分割name，返回值是列表
    tmp = name.split('.')
    vals = {}
    for k in tmp:
        if k in dt:
            vals = dt.get(k, None)
        elif k in vals:
            vals = vals.get(k, None)
        else:
            vals = None
    return vals
