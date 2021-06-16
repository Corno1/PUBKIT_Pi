import sense_hat, time
from sense_hat import SenseHat
import mysql.connector

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
    db.commit()
    time.sleep(1)