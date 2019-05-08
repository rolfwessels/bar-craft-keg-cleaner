
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 5, 6, 12, 13, 17]
"""
2-Air
3_DUMP
4-H2O PMP
5 - H"O
6-SANRECIRC
12-SAN
13-
17-H2O RECIRC
"""

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeRUN = 2

SleepTimeRUNS = 2

try:


      for i in pinList:
         
        GPIO.output(6, GPIO.LOW)
        print ('RECIRC 1 ON')
        time.sleep(SleepTimeRUN);
                
        GPIO.output(6, GPIO.HIGH)
        time.sleep(SleepTimeRUNS);
        print ('PMP 2 OFF')
         
         

    
       
          


# End program cleanly with keyboard
except KeyboardInterrupt:
  'print' "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
         
         
         


         
         
         
