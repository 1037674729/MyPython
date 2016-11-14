
import MySQLdb
import sys

class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn


    def check_acct_available(self,acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from pay where acctid=%s" % acctid
            cursor.execute(sql)
            print "check_acct_avilable:" + sql
            result = cursor.fetchall()
            if len(result) != 1:
                raise Exception("Account %s does not exist" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from pay where acctid=%s and money>%s" % (acctid,money)
            cursor.execute(sql)
            print "has_enough_money:" + sql
            result = cursor.fetchall()
            if len(result) != 1:
                raise Exception("Account %s amount is less than" % acctid)
        finally:
            cursor.close()


    def reduce_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update pay set money= money - %s where acctid=%s" % (money,acctid)
            cursor.execute(sql)
            print "reduce_money:" + sql
            # result = cursor.rowcount()
            if cursor.rowcount != 1:
                raise Exception("Account %s reduce failed" % acctid)

        finally:
            cursor.close()



    def add_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update pay set money= money + %s where acctid=%s" % (money,acctid)
            cursor.execute(sql)
            print "add_money:" + sql
            # result = cursor.rowcount() python的变量不能重写,也就是说result不能用到cursor.rowcount那里去.
            if cursor.rowcount != 1:
                raise Exception("Account %s add failed" % acctid)

        finally:
            cursor.close()


    def transfer(self,source_acctid,target_acctid,money):
        try:
            self. check_acct_available(source_acctid)
            self.check_acct_available(target_acctid)
            self.has_enough_money(source_acctid,money)
            self.reduce_money(source_acctid,money)
            self.add_money(target_acctid,money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ =="__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.Connect(host = '127.0.0.1', port = 3306,user = 'root',passwd = 'root',db = 'philips')

    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print "go wrong: " + str(e)
    finally:
        conn.close()



