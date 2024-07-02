import mysql.connector
import sys
#Function for connecing in database:
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
#Function for registering driver in database:
def insert(driver):
    conn = None
    sql = """INSERT INTO drivers (Name,Email,Address,Mobile,LicenseNo,Password) VALUES(%s,%s,%s,%s,%s,%s)"""
    values = (driver.getName(),driver.getEmail(),driver.getAddress(),driver.getMob(),driver.getLice(),driver.getPasswo())
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
#Function for viewing booking:
def search():
    sql = """SELECT * FROM books"""
    records = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error:",sys.exc_info())
    finally:
        del sql
        del conn
        return records