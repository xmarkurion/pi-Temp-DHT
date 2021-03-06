# Simple DHT TEMP HUM reading program. 
# Collecting data for 5 min then save the data to CSV data file.

import lcddriver
import time
import datetime
import Adafruit_DHT
import sys
import random
import os.path

display = lcddriver.lcd()

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg


if os.path.isfile('data.csv'):
    print('File data.csv - Found!')
else:
    with open("data.csv", "a") as f:
        data = ("Day,Time,Temperature,Humidity\n")
        f.write(data)
        f.close()
    print('File not found. Creating file - data.csv')


try:
    temps_list = []  #Init a list of temps
    hums_list = []  #init a list of hums
    x = 0

    # Write line of text to first line of display
    display.lcd_clear()
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    display.lcd_display_string("By - Markurion ", 2) 
    
    while True:       
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

        # Sometimes sensor detect humidity at 3000%
        if humidity is not None and temperature is not None:
            if humidity<100 and temperature<100:
                czas = time.strftime(" %H:%M     %d/%m")
                temps = round(temperature,2)
                hums = round(humidity,2)
                
                print("{0} - {1} - T:{2}, H:{3}".format(x,czas,str(temps),str(hums)))

                #LCD Display data Block BEGIN
                display.lcd_display_string("T:{0} H:{1}".format(str(temps),str(hums)),1)
                display.lcd_display_string(czas,2)
                #END
                time.sleep(1)

                #Save data to table or file if needed
                temps_list.append(temps)
                hums_list.append(hums)

                if x >= 300:
                    avg_temp = cal_average(temps_list)
                    avg_hum = cal_average(hums_list)
                    print("Avg Temp: {0} Avg Hum: {1}".format(round(avg_temp,2),round(avg_hum,2)))

                    with open("data.csv", "a") as f:
                        data = time.strftime("%m/%d/%Y,%H:%M:%S") + "," + str(round(avg_temp,2)) + "," + str(round(avg_hum,2)) + "\n"
                        f.write(data)
                        f.close()

                    x=0
                    del temps_list[:]
                    del hums_list[:]
                else:
                    x+=1

                
        else:
                print('Read Error... 404')

# Exit the program and cleanup
except KeyboardInterrupt: 
    print("Cleaning up!")
    display.lcd_clear()

