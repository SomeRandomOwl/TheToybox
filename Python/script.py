import sqlite3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def printFunction(channel):

	print(“Button 1 pressed!”)
	print(“Note how the bouncetime affects the button press”)

GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=300)

while True:

	GPIO.wait_for_edge(24, GPIO.FALLING)
	print(“Button 2 Pressed”)
	GPIO.wait_for_edge(24, GPIO.RISING)
	print(“Button 2 Released”)

GPIO.cleanup()

sqlite_file = 'coin.db'
# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Inserts an ID with a specific value in a second column 
c.execute("INSERT INTO History (coin, mode, ammount, newTotal, date) VALUES ('Quarter', 'addition', 124, '32$', (CURRENT_TIMESTAMP))")
c.execute("INSERT INTO Quarters (Ammount, Value) VALUES (124, '32$')")
conn.commit()
conn.close()