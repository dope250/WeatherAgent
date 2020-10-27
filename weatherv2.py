#install me with crontab -e:
#*/1 * * * *  /usr/bin/python /home/pi/weatherv2.py >/dev/null 2>&1

import Adafruit_DHT
import pymongo #installed via python -m pip install pymongo
import datetime
import base64
from io import BytesIO



mClient = pymongo.MongoClient("mongodb://192.168.5.93:27017")
#TODO: Credentials

mDB = mClient["weatherData"]
mCol = mDB["devbot"]


sensor = Adafruit_DHT.DHT22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
currentTime = datetime.datetime.now()

DocToInsert = { "datetime": currentTime, "location": { "long": 6.84648, "lat": 51.517019 }, "weatherData": { "temp": temperature, "humidity": humidity } }
x = mCol.insert_one(DocToInsert)
