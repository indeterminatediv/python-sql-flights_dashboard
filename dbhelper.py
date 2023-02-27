import mysql.connector
class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connector error')
    
    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        select distinct(Destination) from flights.flights
        union
        select distinct(Source) from flights.flights
        """)
        data = self.mycursor.fetchall()
        
        for item in data:
            city.append(item[0])
        return city    
    
    def fetch_all_flights(self , source , destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_Time , Duration,Price FROM flights.flights
        where source  = '{}' and Destination = '{}'
        """.format(source,destination))
        data = self.mycursor.fetchall()
        return data   
        