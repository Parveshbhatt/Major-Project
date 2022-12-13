import time
import datetime
import Adafruit_DHT
# from Adafruit_Python_DHT.examples.importGS import *
from script.readGoogleSheet import *
# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT22

DHT_PIN  = 4
# Google Docs spreadsheet name.
worksheet = None
def getData(fileName):
    worksheet = read_csv(fileName)
    if(worksheet == None):
        return []
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).
    if humidity is None or temp is None:
        return[]
    try:
        worksheet.insert_row((datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M'), round(temp, 2), round(humidity, 2)), 1)
        thData = [datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M'), round(temp, 2), round(humidity, 2)]
        return thData
    except: 
        print('Append error, logging in again')
        return []
