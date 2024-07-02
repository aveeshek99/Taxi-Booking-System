import mysql.connector
import sys
#Function for connecting to database:
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='taxi'
        )
    except:
        print("Error:",sys.exc_info())
    finally:
        return conn
#Function for editing password of customer/driver:
def edit(passwo,email):
    try:
        sql = """UPDATE customers SET Password=%s WHERE Email=%s"""
        values = (passwo,email)
        result = False
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        result = False
    finally:
        del sql
        del values
        return result
        