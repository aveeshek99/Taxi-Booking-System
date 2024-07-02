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
#Function for insering booking info in database:
def insert(Book):
    conn = None
    sql = """INSERT INTO books (Pickup,Dropoff,Date,Payment) VALUES(%s,%s,%s,%s)"""
    values = (Book.getPickup(),Book.getDropoff(),Book.getDate(),Book.getPayment())
    result = False
    try:
        conn= connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error",sys.exc_info())
    finally:
        del values
        del conn
        del sql
        return result
#Function for searching booking info in database:
def search(pick,drop):
    sql = """SELECT * FROM books WHERE Pickup=%s and Dropoff=%s"""
    records = None
    values = (pick,drop,)
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return records
#Function for cancelling booking:
def delete(pick,drop):
    sql = """DELETE FROM books WHERE Pickup=%s and Dropoff=%s"""
    values = (pick,drop,)
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
