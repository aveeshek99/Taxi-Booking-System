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
#Function for logging in as customer,driver and admin:
def search(email,password):
    #Code for checking in customer database for login:
    sql = """SELECT * FROM customers WHERE Email=%s and Password=%s"""
    records = None
    values = (email,password,)
    result = False
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql,values)
    records = cursor.fetchall()
    if records == []:
        result = False
    else:
        result = True
    cursor.close()
    conn.close()
    del values
    del sql
    del conn
    if result == True:
        return 1
    #Code for checking in driver database for login:
    sql = """SELECT * FROM drivers WHERE Email=%s and Password=%s"""
    records = None
    values = (email,password,)
    result = False
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql,values)
    records = cursor.fetchall()
    if records == []:
        result = False
    else:
        result = True
    cursor.close()
    conn.close()
    del values
    del sql
    del conn
    if result == True:
        return 2
    #Code for checking in admin database for login:
    sql = """SELECT * FROM admin WHERE Email=%s and Password=%s"""
    records = None
    values = (email,password,)
    result = False
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql,values)
    records = cursor.fetchall()
    if records == []:
        result = False
    else:
        result = True
    cursor.close()
    conn.close()
    del values
    del sql
    del conn
    if result == True:
        return 3
    
    
    