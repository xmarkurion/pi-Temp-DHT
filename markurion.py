# Simple clock program. Writes the exact time.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
import lcddriver
import time
import datetime
import Adafruit_DHT

display = lcddriver.lcd()

try:
    print("Writing to Display")
    display.lcd_display_string("Program Start ", 1) 
    # Write line of text to first line of display
    
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        temp = (round(temperature,2))
        hum = (round(humidity,2))
        stringi = "T:" + str(temp) + " H:" + str(hum)
        czas = time.strftime("%H:%M:%S %d/%m")

        display.lcd_display_string(stringi,1)
        print(stringi + " " + czas)
        display.lcd_display_string(czas,2)

        #Save data to scv file
#       with open("data.csv", "a") as f:
#               data = time.strftime("%m/%d/%Y,%H:%M:%S") + "," + str(temp) + "," + str(hum) + "\n"
#               f.write(data)
#               f.close()

        #display.lcd_display_string(str(datetime.datetime.now().time()), 2) # Write just the time to the display
        # Program then loops with no delay (Can be added with a time.sleep)
        #time.sleep(2)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

