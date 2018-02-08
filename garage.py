import RPi.GPIO as GPIO
import time
from email.mime.text import MIMEText
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 7
GPIO_ECHO = 11
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
 
#INFO FOR SENDING TEXT METHOD
me = "your email"
to = ""your phone number"@vtext.com"
login = "your gmail address"
password = "your password"
smptserver = "smtp.gmail.com:587"

#SENDING TEXT METHOD
def sendemail(sender, to, message, login, password, smptserver):
	server = smtplib.SMTP(smptserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(sender, to, message) 
 
#DISTANCE METHOD
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    if (distance > 100):
     sendemail(me, to, message, login, password, smptserver)
     else:
     return distance
      
      

if __name__ == '__main__':
   # try:
       # while True:
           # dist = distance()
           # print ("Measured Distance = %.1f cm" % dist)
           # time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
