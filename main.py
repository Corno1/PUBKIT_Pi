import sense_hat, random, time
from sense_hat import SenseHat
sense = SenseHat()
from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
  host="database-1.c2ggfvafdmjq.us-east-1.rds.amazonaws.com",
  user="admin",
  password="START123!",
  database="ITINFRA"
)
cursor = db.cursor()

while True:
    temp = sense.get_temperature()
    timestamp = datetime.now()
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    statement = "INSERT INTO Data (Timestamp, Temp) VALUES ({}, {})".format(timestamp, temp)
    cursor.execute(statement)
    print(temp)
    time.sleep(1)