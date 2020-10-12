# Simple DHT TEMP HUM reading program. 
# Collecting data for 5 min then save the data to CSV data file.

import lcddriver
import time
import datetime
import Adafruit_DHT
import sys
import random

display = lcddriver.lcd()
display.lcd_clear()

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

    temps = []  #Init a list of temps
    hums = []  #init a list of hums
    
    # Write line of text to first line of display
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    display.lcd_display_string("By - Markurion ", 2) 
    time.sleep(1)
    
    while True:
        try:
            for x in range(100):
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

                # Sometimes sensor detect humidity at 3000%
                if humidity is not None and temperature is not None:
                    if humidity<100 and temperature<100:
                        temps.insert(x,round(temperature,2))
                        hums.insert(x,round(humidity,2))
                
                        print("{0} - T:{1}, H:{2}".format(x,temps[x],hums[x]))
                        print("{0} - T:{1}, H:{2}".format(x,temperature,humidity))
                        print("\n")

                        #LCD Display data Block BEGIN
                        display.lcd_display_string("T:{0} H:{1}".format(temps[x],hums[x]),1)
                        czas = time.strftime(" %H:%M     %d/%m")
                        display.lcd_display_string(czas,2)
                        #END
                        #time.sleep(2)
                else:
                    print('Read Error... 404')
                
            #Read Average And save those to CSV      	    
            avg_temp = cal_average(temps)
            avg_hum = cal_average(hums)
            print("Avg Temp: {0} Avg Hum: {1}".format(round(avg_temp,2),round(avg_hum,2)))

            #Savee data to scv file
            with open("data.csv", "a") as f:
                data = time.strftime("%m/%d/%Y,%H:%M:%S") + "," + str(round(avg_temp,2)) + "," + str(round(avg_hum,2)) + "\n"
                f.write(data)
                f.close()
            #--------------------------------------

            # Clear list of values
            del temps[:]
            del hums[:]

        except EnvironmentError:
            print("DHT sensor had a bad time Try again later")

        except KeyboardInterrupt:
            display.lcd_clear()


# Exit the program and cleanup
# except KeyboardInterrupt: 
#     print("Cleaning up!")
#    

