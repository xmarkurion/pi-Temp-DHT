# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
import lcddriver
import time
import datetime
import Adafruit_DHT
import sys

display = lcddriver.lcd()

try:
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    display.lcd_display_string("By - Markurion ", 2) 
    # Write line of text to first line of display
    
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

        if humidity is not None and temperature is not None:
            #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            temp = "{0:.1f}".format(temperature)
            hum = "{0:.2f}".format(humidity)
            stringi = "T:" + str(temp) + " H:" + hum + "  "
            #czas = time.strftime("%H:%M:%S %d/%m")+ "  "
            czas = time.strftime(" %H:%M     %d/%m")

            display.lcd_display_string(stringi,1)
            print(stringi + " " + czas)
            display.lcd_display_string(czas,2)
            time.sleep(1)
        

        #Savee data to scv file
#       with open("data.csv", "a") as f:
#               data = time.strftime("%m/%d/%Y,%H:%M:%S") + "," + str(temp) + "," + str(hum) + "\n"
#               f.write(data)
#               f.close()

        #display.lcd_display_string(str(datetime.datetime.now().time()), 2) # Write just the time to the display
        # Program then loops with no delay (Can be added with a time.sleep)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

