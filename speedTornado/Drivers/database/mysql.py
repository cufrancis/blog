#!/usr/bin/env Python
# coding=utf-8

import sys
sys.path.append('../../../')

from speedTornado.config import Config
import pymysql


class db_mysql(object):

    # 数据库连接句柄
    conn = ''
    cursor = ''

    # 执行的SQL语句记录
    arrSql = [] #列表

    # 返回值是列表，列表内包含字典
    def getList(self, sql = ''):
        return self.exec_(sql)

    # 返回最后更新的行id
    def newinsertid(self):
        return self.cursor.lastrowid

    def setlimit(self, sql = '', limit = ''):
        return sql + ' LIMIT {limit}'.format(limit=limit)

    # 执行sql 语句，并返回列表数据
    def exec_(self, sql = ''):
        self.arrSql.append(sql)

        self.cursor.execute(sql)
        self.conn.commit() #commit, update insert, delete
        # print(sql)
        result = self.cursor.fetchall()

        return result

    # 返回影响行数
    # Done
    def affected_rows(self):
        # print(self.cursor.rownumber)
        return self.cursor.rowcount


    def getTable(self, tbl_name = ''):
        pass

    # 转义特殊字符，防止数据库注入
    # Undone
    def _val_escape(self, value):
        return value

    # 构造函数
    def __init__(self):
        self.conn = pymysql.connect(host=Config['db']['host'],
                                    user=Config['db']['user'],
                                    password=Config['db']['password'],
                                    db=Config['db']['database'],
                                    charset=Config['db']['charset'],
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        print('Mysql db')
