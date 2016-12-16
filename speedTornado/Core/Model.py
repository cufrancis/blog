#!/usr/bin/env Python
# coding=utf-8
#
import sys
sys.path.append('../../')
# sys.path.append('../Drivers/')# 增加驱动搜索目录

import importlib

from speedTornado.config import Config
from speedTornado.Drivers.database import *

class Model(object):

    # 表名称
    # table = ''

    # 表主键
    pk = 'id'

    # 表全名
    # tbl_name = ''

    # 存储驱动程序
    # _db = ''

    # 构造函数
    def __init__(self):
        if len(self.tbl_name) == 0:
            self.tbl_name = Config['db']['prefix'] + self.table
        if len(Config['db_driver_path']) == 0:
            Config['db_driver_path'] = Config['st_drivers_path'] + '/' + Config['db']['driver'] + '.py'

        # Todo:::Lab Test
        # if len(Config['db']['driver']) != 0:
        #     self._db = importlib.find_loader("db_"+Config['db']['driver'])

        self._db = eval('db_' + Config['db']['driver'])()

    # 查找一条记录
    # Done
    def find(self, conditions = {}, sort = '', fields = ''):
        result = self.findAll(conditions, sort, fields, '1')

        # print(help(self._db._val_escape))

        if len(result) != 0:
            # 这里返回的依然是字典，程序需要result[0]['username']才能获取数据
            # 未完成：
            # 以后可以将列表转换成字典，直接使用result['username']获取数据
            return result
        else:
            return False

    # conditions 可以是字典或者字符串
    # Done
    def findAll(self, conditions = {}, sort = '', fields = '', limit = ''):
        where = 'WHERE '
        fields = "*" if len(fields) == 0 else fields
        if (isinstance(conditions, dict)):
            join = []
            for k, v in conditions.items():
                v = self.escape(v)
                join.append("{0}='{1}'".format(k, v))

            # print(join)
            num = len(join)
            tmp = ''
            while (num > 0):
                num = num - 1
                if num != 0:
                    tmp = tmp + join[num] + ' AND '
                else:
                    tmp = tmp + join[num]
                # print(num)
            # print(tmp)

            where = where + tmp
            # print(where)
        else:
            if len(conditions) != 0:
                where = where + conditions
        if len(sort) != 0:
            sort = "ORDER BY {sort}".format(sort=sort)
        else:
            sort = "ORDER BY {0}".format(self.pk)

        sql = "SELECT {fields} FROM {tbl_name} {where} {sort}".format(fields = fields, tbl_name = self.tbl_name, where = where,sort = sort)

        # print(sql)

        if len(limit) != 0:
            sql = self._db.setlimit(sql, limit)
        return self._db.getList(sql)


    # 过滤转义字符
    def escape(self, value):
        # return value
        return self._db._val_escape(value)

    # __val_escape 是 val 的别名
    # Done
    def _val_escape(self, value):
        return self.escape(value)

    # 数据库增加，输入字典
    # Done
    def create(self, row = {}):
        # 不是字典，返回False
        if isinstance(row, dict) == False:
           return False

        if len(row) == 0:
            return False

        cols = ''
        vals = ''
        sql = ''
        for k, v in row.items():
            cols = cols +  ',' + k
            # vals = vals + ',' + self.escape(v)
            vals = "{vals}, '{v}' ".format(vals=vals, v=self.escape(v))
        cols = cols[1:]
        vals = vals[1:]

        sql = "INSERT INTO {tbl_name} ({cols}) VALUES ({vals})".format(tbl_name=self.tbl_name, cols=cols, vals=vals)

        # 插入数据完成
        # Done
        if self._db.exec_(sql) != False:
            newinsertid = self._db.newinsertid()
            if newinsertid:
                return newinsertid
            else:
                return False
        else:
            return False

    # 输入list
    # Done
    # Todo:
    # 自动将输入的字典转换成list，防止用户输入错误数据
    # 返回值： 新id列表
    def createAll(self, rows = {}):
        num = len(rows)
        # print(num)
        newid = []
        while num > 0:
            num = num -1
            newid.append(self.create(rows[num]))
        return newid

    # 删除数据，输入条件为字典
    # 返回影响行数，无影响返回0
    # Done
    def delete(self, conditions = {}):
        where = ''
        if isinstance(conditions, dict):
            join = []
            condition = ''
            for k, v in conditions.items():
                condition = self.escape(v)
                join.append("{key}='{condition}'".format(key=k, condition=condition))

            # print(join)
            num = len(join)
            tmp = ''
            while num > 0:
                num = num - 1
                if num != 0:
                    tmp = tmp + join[num] + ' AND '
                else:
                    tmp = "{tmp}{join}".format(tmp=tmp, join=join[num])

            # print(tmp)
            where = 'WHERE ( {join} )'.format(join=tmp)
            # print(where)
        else:# no dict
            if len(conditions):
                where = "WHERE ({join})".format(join=conditions)
        sql = "DELETE FROM {tbl_name} {where}".format(tbl_name=self.tbl_name, where=where)
        # print(sql)
        self._db.exec_(sql)
        # 返回影响行数，无影响返回0
        return self._db.affected_rows()

    # 按字段查找一条记录
    # Done
    # Todo:
    # 不确定有没有存在的必要，和find功能一样，只是输入数据格式不同
    def findBy(self, field = '', value = ''):
        # where = {}
        where = {field :value}
        return self.find(where)

    def updateField(self, conditions = '', field = '', value = ''):
        pass

    # 使用sql 进行查找操作，等于进行find, findAll等操作，高级定制功能
    # Done
    def findSql(self, sql = ''):
        return self._db.getList(sql)

    # 运行SQL语句，相当于INSERT, UPDATE, DELETE等操作，高级定制功能
    # Done
    def runSql(self, sql = ''):
        return self._db.exec_(sql)

    # 向前兼容
    # Done
    def query(self, sql = ''):
        return self.findSql(sql)

    # 返回最后执行的 Sql 语句供执行
    # Done
    def dumpSql(self):
        return self._db.arrSql

    # 返回上次执行Update，Create, Delete, Exec_的影响行数
    # Undone
    # Todo:::
    # Create时返回数据不准确，待解决
    def affectedRows(self):
        return self._db.affected_rows()

    # 计算符合条件的记录数量
    # 只返回数字
    # Done
    def findCount(self, conditions = {}):
        where = ''
        # print(conditions)
        if isinstance(conditions, dict):
            join = []
            for k, v in conditions.items():
                condition = self.escape(v)
                join.append("{key} = '{condition}'".format(key=k, condition=condition))

            num = len(join)
            tmp = ''

            while num > 0:
                num = num -1
                if num != 0:
                    tmp = "{tmp}{join} AND ".format(tmp=tmp, join=join[num])
                else:
                    tmp = "{tmp}{join}".format(tmp=tmp, join=join[num])

            where = 'WHERE {join}'.format(join=tmp)
        else:
            if len(conditions) > 0:
                where = 'WHERE {join}'.format(join=conditions)

        sql = "SELECT COUNT({pk}) AS ST_COUNTER FROM {tbl_name} {where}".format(pk=self.pk, tbl_name=self.tbl_name, where=where)
        result = self._db.exec_(sql)
        # 返回整数
        print(result[0]['ST_COUNTER'])

    # 根据给定的conditions 更新row
    # conditions:dict, row:dict
    #
    # 返回执行影响的行数，无影响返回0，失败返回False
    # 注意：返回0不代表执行失败，只是没有数据可修改
    #
    # Done
    # Todo:::Refactoring
    # 处理逻辑太复杂，有很多重复的步骤，比如将列表转换成字符串部分可以提取出来
    def update(self, conditions = {}, row = {}):
        where = ''
        # print(conditions)
        if len(row) <= 0:
            return False

        if isinstance(conditions, dict):
            join = []
            for k, v in conditions.items():
                condition = self.escape(v)
                join.append("{key} = '{condition}'".format(key=k, condition=condition))

            num = len(join)
            tmp = ''
            while num > 0:
                num = num - 1
                if num != 0:
                    tmp = "{tmp}{join} AND".format(tmp=tmp, join=join[num])
                else:
                    tmp = "{tmp}{join}".format(tmp=tmp, join=join[num])

            where = 'WHERE {join}'.format(join=tmp)
        else:
            if len(conditions) != 0:
                where = 'WHERE {join}'.format(join=conditions)

        # return where
        vals = []
        # 要修改的 参数:值 字典
        for k, v in row.items():
            val = self.escape(v)
            vals.append("{key} = '{value}'".format(key=k, value=val))

        num = len(vals)
        values = ''
        while num > 0:
            num = num - 1
            if num != 0:
                values = "{values}{vals} ,".format(values=values, vals=vals[num])
            else:
                values = "{values}{vals}".format(values=values, vals=vals[num])

        sql = "UPDATE {tbl_name} SET {values} {where}".format(tbl_name=self.tbl_name, values=values, where=where)
        self._db.exec_(sql)
        return self._db.affected_rows()

    # 功能有待确定，暂不添加
    # def replace(self, conditions = {}, row = {}):
    #     pass

    # 为设定的字段增加
    # conditions:dict, field:str, optval:int
    #
    # 返回影响的行数，无影响返回0
    # Done
    def incrField(self, conditions = {}, field = '', optval = 1):
        where = ''
        if isinstance(conditions, dict) == False:
            return False
        join = []
        for k, v in conditions.items():
            condition = self.escape(v)
            join.append("{key} = '{condition}'".format(key=k, condition=condition))

            num = len(join)
            tmp = ''
            while num > 0:
                num = num - 1
                if num != 0:
                    tmp = "{tmp}{join} AND ".format(tmp=tmp, join=join[num])
                else:
                    tmp = "{tmp}{join}".format(tmp=tmp, join=join[num])
            where = 'WHERE {join}'.format(join=tmp)
            # else:
        # if len(conditions) != 0:
        #
        #     where = 'WHERE {join}'.format(join=conditions)

        values = "{field} = {field} + {optval}".format(field=field, optval=optval)
        sql = "UPDATE {tbl_name} SET {values} {where}".format(tbl_name=self.tbl_name, values=values, where=where)
        # return sql
        self._db.exec_(sql)
        return self.affectedRows()

    # 按照给定的字段减少值
    # 函数实现和 incrField 一样
    # Done
    def decrField(self, conditions = {}, field = '', optval = 1):
        return self.incrField(conditions, field, -optval)

    # 按给定的数据表的主键删除记录
    def deleteByPk(self, pk = ''):
        return self.delete({self.pk:pk})

# db = Model()
# # print(help(db._db))
# result = db.find({'username':'cufrancis'})
# print(result)
