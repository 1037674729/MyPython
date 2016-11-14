# -*- coding:UTF8 -*-
import MySQLdb
import sys

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'philips',
    charset = 'utf8'
)



class SQLputer(object):

    def __init__(self):
        self.sqldata = []
        self.conn =  MySQLdb.Connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = 'root',
            db = 'philips',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()



    def collect_data(self,data):
        if data is None:
            return
        self.sqldata.append(data)

    def output_sql(self):
        try:
            for data in self.sqldata:
                insert_sql = "insert into philips_user(username,password,telphone)" \
                             "values('%s','%s','$s')" % (data['url'].encode('utf-8'),data['title'].encode('utf-8'),data['summary'].encode('utf-8'))

                self.cursor.execute(insert_sql)
                self.conn.commit()  # 执行提交数据到数据库中.
                if self.conn.conmit !=1:
                    raise Exception("%s 加入数据库失败"% data['url'])
        finally:
            self.cursor.close()


