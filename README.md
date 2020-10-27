# Weather Agent 
python script for a raspberry pi with DHT22.
Sends temperature and humidity data to a mongoDB.

## Prerequisites
  * Python 2.7.16 & pip
  * pymongo
  * Adafruit_DHT

## Install

Install pymongo:
python -m pip install pymongo

Install Adafruit_DHT:
  * TODO

Change connection to mongoDB.
Then install me with crontab -e to send every minute some data:
*/1 * * * *  /usr/bin/python /home/pi/weatherv2.py >/dev/null 2>&1

## Requirements
  * Raspberry Pi (tested with zero w)
  * DHT22

