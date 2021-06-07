import psycopg2
def connect():
    try:
        conn=psycopg2.connect(user="aacreetiee",password="aaku",database="kct",host="localhost",port=5432)
        print("The database is connected")
    except psycopg2.Error as e:
        print(e)
    finally:
        conn.close()
    
if __name__=='__main__':
    connect()