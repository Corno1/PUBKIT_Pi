import sense_hat, random, time
from sense_hat import SenseHat
sense = SenseHat()

while True:
  t = sense.get_temperature()

  print(t)
  time.sleep(1)