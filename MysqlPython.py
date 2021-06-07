import mysql.connector

def connect():
    try:
        conn=mysql.connector.connect(host='localhost',database='LOVE', user='aaku',password="aaku")
        if conn.is_connected():
            print("Database is connected successfully.Thankyou!")
    except Error as e:
        print(e)
    finally:
        conn.close()
        
if __name__=='__main__':
    connect()    
    