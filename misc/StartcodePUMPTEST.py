
import RPi.GPIO as GPIO
import time

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

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop


SleepTimePMP = 3

try:
   count = 2
   while (count > 0):

      'print ''   The count is:', count

      for i in pinList:
         
         G
         GPIO.output(13, GPIO.HIGH)
         
         
         print ('End')

           


# End program cleanly with keyboard
except KeyboardInterrupt:
  'print' "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
         
         
         


         
         
         
