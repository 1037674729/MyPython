import MySQLdb

conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'philips',
    charset = 'utf8'
)

cursor = conn.cursor()


insert_sql = "insert into philips_user(username,password,telphone,section,number,status)values('steven','123456','123321123','kehubu','123123',1)"
update_sql = "update philips_user set username='littlefolwer' where id=5"
delete_sql = "delete from philips_user where d=3"

# 放到异常处理里面
try:
    cursor.execute(insert_sql)
    cursor.execute(update_sql)
    cursor.execute(delete_sql)
    conn.commit() #执行提交数据到数据库中.

except Exception as e:
    print e
    conn.rollback()#回滚异常

conn.close()
cursor.close()

