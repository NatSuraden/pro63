import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                password="BFCqhr46914", 
                                host="node4943-env-2254395.th.app.ruk-com.cloud", 
                                port="5432", 
                                database="pythonlogin")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO goldth (D_M_Y,hard_buy, hard_sell, pic_buy,pic_sell) VALUES (%s,%s,%s,%s,%s)"""
    record_to_insert = ('12/10/20','28,250.00', '28,350.00','27,742.00','28,850.00')
    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully in students table")

except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record into students table", error)

finally:
    #closing database connection
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")