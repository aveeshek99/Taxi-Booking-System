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
#Function for registering customer in database:
def insert(customer):
    conn = None
    sql = """INSERT INTO customers (Name,Email,Address,Mobile,Password) VALUES(%s,%s,%s,%s,%s)"""
    values = (customer.getName(),customer.getEmail(),customer.getAddress(),customer.getMob(),customer.getPasswo())
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
