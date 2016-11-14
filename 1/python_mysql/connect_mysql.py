import MySQLdb


conn = MySQLdb.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    charset = 'utf8',
    db = 'philips'
)

cursor = conn.cursor()



# sql = "select * from philips_user";
# cursor.execute(sql)
# print cursor.rowcount
#
# re = cursor.fetchone()
# print re
#
# reman = cursor.fetchmany(3);
# print reman
#
# reall = cursor.fetchall();
# print reall


# cursor.close()
# conn.close()


