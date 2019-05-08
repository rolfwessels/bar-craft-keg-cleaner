#!/usr/bin/env python
import time
import sys
import signal
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#buttons
TANK_1_DUMP=[19]
BUTTON_1 = [20]
BUTTON_2 = [21]
BUTTON_3 = [26]
START = [16]

#CLEANING PUMPS AND SOLONOIDS pinList = [2, 3, 4, 5, 6, 12, 13, 17]
PUMP_1= [13]
PUMP_2= [5]
CIRC_1= [6]
CIRC_2= [17]
DUMP= [3]
AIR= [4]



GPIO.setup(TANK_1_DUMP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_1 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_3 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(START , GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(PUMP_1, GPIO.OUT)
GPIO.output(PUMP_1, GPIO.HIGH)
GPIO.setup(PUMP_2, GPIO.OUT)
GPIO.output(PUMP_2, GPIO.HIGH)
GPIO.setup(CIRC_1, GPIO.OUT)
GPIO.output(CIRC_1, GPIO.HIGH)
GPIO.setup(CIRC_2, GPIO.OUT)
GPIO.output(CIRC_2, GPIO.HIGH)
GPIO.setup(AIR, GPIO.OUT)
GPIO.output(AIR, GPIO.HIGH)
GPIO.setup(DUMP, GPIO.OUT)
GPIO.output(DUMP, GPIO.HIGH)

#First & Final rinse
SleepTimeDELAY = 6
SleepTimeDMP = 22
SleepTimeDMP2 = 15
SleepTimePRIME = 40
SleepTimeRUN = 8

#sanatizer phase
SleepTimeSANDLY = 4
SleepTimeSANDMP = 22
SleepTimeSANDMP2 = 18
SleepTimeSANPRIME = 22
SleepTimeSANRUN = 50

#Clearing
SleepTimeCLRDLY = 8
SleepTimeCLRPRIME = 10
SleepTimeCLRRUN = 15
SleepTimeCLRDMP = 10

print (GPIO.input(19))
print (GPIO.input(20))
print (GPIO.input(21))
print (GPIO.input(26))
print (GPIO.input(16))
print (GPIO.input(13))
print (GPIO.input(3))
print (GPIO.input(4))
print (GPIO.input(5))
print (GPIO.input(6))
print (GPIO.input(17))


try:
    
   run = 0
   while True :
      if GPIO.input(26) ==0 and run == 0:
         print ("  Started")
         print ('Clearing...')
         
         GPIO.output(4, GPIO.LOW)
         print ('AIR ON...')
         time.sleep(SleepTimeCLRDLY);
                 
         GPIO.output(3, GPIO.LOW)
         print ('DUMP ON...')
         time.sleep(SleepTimeCLRRUN);
         
         
         GPIO.output(4, GPIO.HIGH)
         print ('AIR ...OFF')
         time.sleep(SleepTimeCLRPRIME);
         GPIO.output(3, GPIO.HIGH)
         print ('DMP ...OFF')
        
       while GPIO.input(26) ==0:
             time.sleep(0.2)
      if GPIO.input(26) ==1 and run == 0:
         print ("  Stopped ")
         
         break
         
         
         while GPIO.input(26) ==0:
             time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
