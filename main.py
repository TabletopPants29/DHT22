import time 
import datetime
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 18
global temp_old_c
global temp_old_humidity
temp_old_c = float(0.0)
temp_old_humidity = float(0.0)

try:
    while True:
        time.sleep(3)
        try:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                print("Temp={0:.2f}*C  Humidity={1:.2f}".format(temperature, humidity))
                if temp_old_c!=round(temperature,2) and temp_old_humidity!=round(humidity,2):
                    try:
                        file = open("DHT22_1_LOG.DAT","a")
                        file.write("{sensor:'DHT22_1',dated:'"+datetime.datetime.now().strftime("%H:%M:%S")+"',temperature:"+str(round(temperature,2)) +",humidity:"+str(round(humidity,2))+"}\n")
                        file.close()
                        file = open("DHT22_1_CURRENT.DAT","w")
                        file.write("{sensor:'DHT22_1',dated:'"+datetime.datetime.now().strftime("%H:%M:%S")+"',temperature:"+str(round(temperature,2)) +",humidity:"+str(round(humidity,2))+"}\n")
                        file.close()
                       
                        temp_old_c = round(temperature,2)
                        temp_old_humidity = round(humidity,2)
                    except:
                        print("Unable to write to file!")
            else:
                print("Failed to retrieve data from humidity sensor")
        except:
                print("Some Error occured")
except KeyboardInterrupt:
    print("Program terminated by user")
