
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
19-H2O RECIRC
"""

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

    GPIO.setwarnings(False) 

SleepTimeDELAY = 2
SleepTimeDMP = 18
SleepTimeDMP2 = 20
SleepTimePRIME = 22
SleepTimeRUN = 10

try:
      for i in pinList:
         
         GPIO.output(5, GPIO.LOW)
         print ('PUMP 2 ON') 
         time.sleep(SleepTimeDELAY);
                
                
         GPIO.output(3, GPIO.LOW)
         print ('DMP ON')
         time.sleep(SleepTimeDMP);
         
         GPIO.output(3, GPIO.HIGH)
         print ('DMP OFF')
               
         GPIO.output(6, GPIO.LOW)
         print ('RECIRC 2 ON')
         time.sleep(SleepTimeRUN);
         
         
        
         GPIO.output(5, GPIO.HIGH)
         print ('PMP 2 OFF')
         time.sleep(SleepTimeDMP2);
         
         GPIO.output(4, GPIO.LOW)
         print ('AIR ON')
         time.sleep(SleepTimePRIME);
         GPIO.output(4, GPIO.HIGH)
         print ('AIR OFF')
         time.sleep(SleepTimeDMP2);

                 
         GPIO.output(6, GPIO.HIGH)
         print ('RECIRC 2 OFF')
         break
 
         print ("end")
         sys.exit()          
# End program cleanly with keyboard
except KeyboardInterrupt:
  'print' "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
         
         
         


         
         
         
