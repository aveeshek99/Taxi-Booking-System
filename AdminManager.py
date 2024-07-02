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
#Function for displaying all booking info:
def allBooking():
    sql = """SELECT * from books"""
    conn = None
    try: 
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error",sys.exc_info())
    finally:
        del sql
        del conn
        return records
#Function for displaying all driver info:
def allDriver():
    sql = """SELECT * from drivers"""
    conn = None
    try: 
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error",sys.exc_info())
    finally:
        del sql
        del conn
        return records
#Function for cancelling booking:
def deleteBooking(id):
    sql = """DELETE FROM books WHERE BID=%s"""
    values = (id,)
    result = False
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error:",sys.exc_info())
    finally:
        del sql
        del values
        return result