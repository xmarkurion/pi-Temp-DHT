# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
import lcddriver
import time
import datetime
import Adafruit_DHT
import sys
from statistics import mean

display = lcddriver.lcd()

try:
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    display.lcd_display_string("By - Markurion ", 2) 
    # Write line of text to first line of display
    temps = []  #Init a list of temps
    hums = []  #init a list of hums
    
    while True:
        # Clear list of values
        temps.clear()
        hums.clear()
        #---------------------
        #{time.strftime("%H:%M:%S %d/%m")}
        #Initialize 5min delay 
        for x in range(301):
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
            if humidity is not None and temperature is not None:
                temps.append( round(temperature,2) )
                hums.append( round(humidity,2) )
                print("{0} - T:{1}, H:{2}".format(x,temps[x],hums[x]))

                #LCD Display data Block BEGIN
                display.lcd_display_string("T:{0} H:{1}".format(temps[x],hums[x]))
                czas = time.strftime(" %H:%M     %d/%m")
                display.lcd_display_string(czas,2)
                #END

                time.sleep(1)

        #Read Average And save those to CSV      	    
        avg_temp = mean(temps)
        avg_hum = mean(hums)
        print(f'Avg Temp: {round(avg_temp,2)} Avg Hum: {round(avg_hum,2)}')

        #--------------------
        #if humidity is not None and temperature is not None:
            #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            # temp = "{0:.1f}".format(temperature)
            # hum = "{0:.2f}".format(humidity)
            # stringi = "T:" + str(temp) + " H:" + hum + "  "
            #czas = time.strftime("%H:%M:%S %d/%m")+ "  "
            # czas = time.strftime(" %H:%M     %d/%m")

            # display.lcd_display_string(stringi,1)
            # print(stringi + " " + czas)
            # display.lcd_display_string(czas,2)
            # time.sleep(1)
        

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

