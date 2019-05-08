
import RPi.GPIO as GPIO
import time
import sys 

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 5, 6, 12, 13, 19]
"""
2-Air
3_DUMP
4-H2O PMP
5 - H"O
6-SANRECIRC
12-SAN
13-
19-H2O RECIRC
"""

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

GPIO.setwarnings(False) 

SleepTimeAIR = 6
SleepTimeDMP = 10
SleepTimePMP = 6


try:
    
    for i in pinList:
               
         GPIO.output(2, GPIO.LOW)         
         time.sleep(SleepTimeAIR);
         GPIO.output(2, GPIO.HIGH)

         GPIO.output(3, GPIO.LOW)         
         time.sleep(SleepTimeAIR);
         GPIO.output(3, GPIO.HIGH)
        
         sys.exit()     
 
         print ("end")
    

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
GPIO.cleanup()
         
         


         
         
         
