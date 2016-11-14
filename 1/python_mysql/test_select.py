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



sql = "select id,username,section from philips_user";

cursor.execute(sql)

print cursor.rowcount

re = cursor.fetchall();
for row in re:
    print "id=%s,username=%s,section=%s" % row


cursor.close()
conn.close()