import mysql.connector
import datetime
import time
import random

db = mysql.connector.connect(
	host="192.168.2.103",
	user="root",
	passwd="",
	database="test"
)

mycursor = db.cursor()

print(db)

