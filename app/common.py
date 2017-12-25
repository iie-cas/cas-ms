#coding:utf8
import pymysql
from models import Models


# 数据库配置
DB = {
    'user': 'root',
    'passwd': '123456',
    'db': 'score',
    'host': '127.0.0.1',
    'port': 3306,
    'charset':'utf8'
}


def getConn():
    """
    连接数据库
    """
    conn = pymysql.connect(host=DB['host'], port=DB['port'], user=DB['user'],
                            passwd=DB['passwd'], db=DB['db'], charset=DB['charset'])
    return conn


def create_db():
    """
    创建数据表
    """
    conn = getConn()
    with conn as cursor:
        for item in Models:
            cursor.execute(item)
        print("create table finished!")
