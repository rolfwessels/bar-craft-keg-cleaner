
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

SleepTimeAIR = 2
SleepTimeDMP = 2
SleepTimePMP = 2
SleepTimeH2O = 2
SleepTimeSANREC = 2
SleepTimeSAN = 2
SleepTimeH2OREC = 2

try:
   count = 2
   while (count > 0):

      'print ''   The count is:', count

      for i in pinList:
         GPIO.output(17, GPIO.LOW)
         time.sleep(SleepTimeH2OREC);

         GPIO.output(5, GPIO.LOW)
         time.sleep(SleepTimeH2O);

         GPIO.output(4, GPIO.LOW)
         time.sleep(SleepTimePMP);
         GPIO.output(4, GPIO.HIGH)
         GPIO.output(5, GPIO.HIGH)
         
         GPIO.output(2, GPIO.LOW)
         time.sleep(SleepTimeAIR);
         GPIO.output(2, GPIO.HIGH)

         GPIO.output(17, GPIO.HIGH)
          


# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
         
         
         


         
         
         
