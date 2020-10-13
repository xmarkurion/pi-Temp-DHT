# Simple DHT TEMP HUM reading program. 
# Collecting data for 5 min then save the data to CSV data file.

import lcddriver
import time
import datetime
import Adafruit_DHT
import sys
import random

display = lcddriver.lcd()

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg



try:
    temps_list = []  #Init a list of temps
    hums_list = []  #init a list of hums
    x = 0

    # Write line of text to first line of display
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    display.lcd_display_string("By - Markurion ", 2) 
    
    while True:       
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

        # Sometimes sensor detect humidity at 3000%
        if humidity is not None and temperature is not None:
            if humidity<100 and temperature<100:
                temps = round(temperature,2)
                hums = round(humidity,2)
                
                print("T:{0}, H:{1}".format(str(temps),str(hums)))
                print("\n")

                #LCD Display data Block BEGIN
                display.lcd_display_string("T:{0} H:{1}".format(str(temps),str(hums)),1)
                czas = time.strftime(" %H:%M     %d/%m")
                display.lcd_display_string(czas,2)
                #END
                time.sleep(1)

                #Save data to table or file if needed
                temps_list.insert(temps)
                hums_list.insert(hums)
                if x >= 100:
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
                
        #Read Average And save those to CSV      	    
        # avg_temp = cal_average(temps)
        # avg_hum = cal_average(hums)
        # print("Avg Temp: {0} Avg Hum: {1}".format(round(avg_temp,2),round(avg_hum,2)))

        #Savee data to scv file
        # with open("data.csv", "a") as f:
        #     data = time.strftime("%m/%d/%Y,%H:%M:%S") + "," + str(round(avg_temp,2)) + "," + str(round(avg_hum,2)) + "\n"
        #     f.write(data)
        #     f.close()
        #--------------------------------------

        # Clear list of values
        # del temps[:]
        # del hums[:]

# Exit the program and cleanup
except KeyboardInterrupt: 
    print("Cleaning up!")
    display.lcd_clear()

