import mysql.connector
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
    print('connecton error')
mycursor.execute("""
        select distinct(Destination) from flights.flights
        union
        select distinct(Source) from flights.flights
        """)
data = mycursor.fetchall()
city = []
for item in data:
    city.append(item[0])
print(city)   
        