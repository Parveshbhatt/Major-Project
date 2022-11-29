import Adafruit_DHT

import time

#comment and uncomment the lines below depending on your sensor
#sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT22
#sensor = Adafruit_DHT.AM2302

#DHT pin connects to GPIO 4
sensor_pin = 4

#create a variable to control the while loop
running = True

#new .txt file created with header
file = open('dhtReading.csv', 'a')
#file.write('time and date, temperature (C),temperature (F), humidity\n')

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
        
        humidity = "{0:.2f}".format(humidity)
        temperature = "{0:.2f}".format(temperature)

        #uncomment the line below to convert to Fahrenheit
        #temperature_f = temperature * 9/5.0 + 32

        #sometimes you won't get a reading and
        #the results will be null
        #the next statement guarantees that
        #it only saves valid readings
        if humidity is not None and temperature is not None:

            #print temperature and humidity
            print('Temperature = ' + str(temperature) +','+ 'Humidity = ' + str(humidity))
            #save time, date, temperature in Celsius, temperature in Fahrenheit and humidity in .txt file
            file.write(time.strftime('%Y/%m/%d')+ ', ' + time.strftime('%H:%M') + ', ' + str(temperature) + ', '+ str(humidity) + '\n')
            time.sleep(5)

        else:
            print('Failed to get reading. Try again!')
            time.sleep(5)

    except KeyboardInterrupt:
        print ('Program stopped')
        running = False
        file.close()
