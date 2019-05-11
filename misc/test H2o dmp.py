
import RPi.GPIO as GPIO
import time
import sys 

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [4, 3,17]
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

SleepTimeDELAY = 4
SleepTimeDMP = 15
SleepTimePRIME = 25
SleepTimeRUN = 25


try:
    
    for i in pinList:
          
         GPIO.output(4, GPIO.LOW)
         print ('AIR ON')
         time.sleep(SleepTimeDELAY);
                 
         GPIO.output(3, GPIO.LOW)
         print ('DUMP ON')
         time.sleep(SleepTimeRUN);
         
         
         GPIO.output(4, GPIO.HIGH)
         print ('AIR OFF')
         time.sleep(SleepTimePRIME);
         GPIO.output(3, GPIO.HIGH)
         print ('DMP OFF')
         
         
        
         break
         print ("end")
         GPIO.cleanup()
         sys.exit()
 
       
            
     

        
            

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
GPIO.cleanup()
         
         


         
         
         
