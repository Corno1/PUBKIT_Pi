import sense_hat, time
from sense_hat import SenseHat
import mysql.connector
from gps3 import gps3

gps_socket =gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

sense = SenseHat()
db = mysql.connector.connect(
  host="database-1.c2ggfvafdmjq.us-east-1.rds.amazonaws.com",
  user="admin",
  password="START123!",
  database="ITINFRA"
)
cursor = db.cursor()

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        if data_stream.TPV["lon"] != "n/a":
            temp = round(sense.get_temperature(), 1)
            timestamp = round(time.time() *1000)
            statement = "INSERT INTO sensordata (Timestamp, Temp, Lat, Lon) VALUES ({}, {}, {}, {})".format(timestamp, temp, data_stream.TPV['lat'], data_stream.TPV['lon'])
            cursor.execute(statement)
            db.commit()
            time.sleep(1)
            
    
