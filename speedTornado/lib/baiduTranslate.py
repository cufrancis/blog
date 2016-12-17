#!/usr/bin/env Python
# coding=utf-8
import sys
sys.path.append("../../")

# import httplib
import hashlib
import urllib
import random
import requests
import json

from speedTornado.config import Config

class baiduTranslate(object):

    def __init__(self):
        self.appid = Config['baiduTranslate']['appid']
        self.secretKey = Config['baiduTranslate']['secretKey']
        self.myurl = '/api/trans/vip/translate'


    def translate(self, q='', fromLang='', toLang=''):

        s = requests.Session()
        result = json.loads(s.get('http://api.fanyi.baidu.com'+self.myUrl(q, fromLang, toLang)).text)

        # 返回翻译后的字符串
        return result['trans_result'][0]['dst']

    # 生成查询url
    def myUrl(self, q, fromLang, toLang):
        salt = random.randint(32768, 65535)
        sign = self.appid+q+str(salt)+self.secretKey
        sign = sign.encode('utf-8')
        m1 = hashlib.md5()
        m1.update(sign)
        sign = m1.hexdigest()
        return self.myurl+'?appid='+self.appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
