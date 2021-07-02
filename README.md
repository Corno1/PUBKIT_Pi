# PUBKIT_Pi
This is a project for the lecture "planning and operation of complex IT-Infrastructure" of the Ernst-Abbe-Hochschule Jena. The project aims to monitor the distribution of vaccination batches with a Raspberry Pi and a connected Sensehat. 

import sense_hat, random, time
from gps3 import gps3
from sense_hat import SenseHat
import mysql.connector

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
while True:
    temp = round(sense.get_temperature(), 1)
    timestamp = round(time.time() *1000)
    statement = "INSERT INTO sensordata (Timestamp, Temp) VALUES ({}, {})".format(timestamp, temp)
    cursor.execute(statement)
    print(temp)
    print(statement)
    print(db)
    print("Altitude =",data_stream.TPV["alt"])
    print("Longitude =",data_stream.TPV["lon"])
    print("Latitude =",data_stream.TPV["lat"])
    db.commit()
    time.sleep(1)
