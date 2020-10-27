import mysql #install via python -m pip install mysql-connector
import pymongo #installed via python -m pip install pymongo
import mysql.connector
import datetime
import base64
from io import BytesIO

#MongoB
mClient = pymongo.MongoClient("mongodb://192.168.5.93:27017")
mDB = mClient["weatherData"]
mCol = mDB["devbot"]

#MySQL Database
connection = mysql.connector.connect(host = "192.168.5.250", port = "3307", user = "weatherUser", passwd = "InsertPWHere", db = "weather_data")

##Insert Loop

#Fetch count
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM weather")
results = cursor.fetchall()
DataCount = results[0]
print ("Data Entry count: ", DataCount)
LoopCount = 0


#Fetch data
cursor.execute("SELECT create_time, temp, humidity FROM weather")
for x in range(int(DataCount[0])):
        
        print("Entry No.: ", LoopCount)

        results = cursor.fetchone()
        print("Fetched one result:")
        print(results)

        fetchedTime = results[0]
        fetchedTemp = results[1]
        fetchedHumi = results[2]

        #Write Data to Mongo Database
        DocToInsert = { "datetime": fetchedTime, "location": { "long": 6.84648, "lat": 51.517019 }, "weatherData": { "temp": fetchedTemp, "humidity": fetchedHumi } }
        x = mCol.insert_one(DocToInsert)
        LoopCount = LoopCount + 1
##End Loop

connection.close()