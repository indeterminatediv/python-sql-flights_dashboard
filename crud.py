import mysql.connector
# connect to database server
try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'flights'
    )
    mycursor = conn.cursor()
    print('connection established')
except:
    print('connector error')
    
#create a databse on the db server
#mycursor.execute("CREATE DATABASE indigo")    
#conn.commit()

#create a table
#airport --> airport_id / code / name
#mycursor.execute("""
#CREATE TABLE airport(
 #   airport_id INTEGER PRIMARY KEY,
  #  code VARCHAR(10) NOT NULL,
   # city VARCHAR(50) NOT NULL,
  #  name VARCHAR(255) NOT NULL) 
#""")
#conn.commit() 
# insert data to the table
#mycursor.execute("""
#                INSERT INTO airport VALUES
#                (1,'DEL','New Delhi','IGIA'),
#                 (2,'CCU','Kokata','NSCA'),
#                (3,'BOM','Mumbai','CSMA')
#""")
#conn.commit()

#search/retreive
# mycursor.execute("select * from airport WHERE airport_id > 1")
# data = mycursor.fetchall()
# print(data)

#update
# mycursor.execute("""
# UPDATE airport
# SET name = 'Bombay'
# where airport_id = 3""")
# conn.commit()

#delete
# mycursor.execute("""
#                  DELETE FROM airport where airport_id = 3
#                  """)
# conn.commit()



             


