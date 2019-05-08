
import RPi.GPIO as GPIO
import time
import sys 

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [4, 3, 5, 6, 13,]
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
SleepTimeDMP = 180
SleepTimePRIME = 25
SleepTimeRUN = 50


try:
    
    for i in pinList:
          
         
         GPIO.output(5, GPIO.LOW)
         print ('PUMP 2 ON...') 
         time.sleep(SleepTimeDELAY);
         GPIO.output(3, GPIO.LOW)
         print ('DMP ON...')
         time.sleep(SleepTimeDMP);
         
         GPIO.output(3, GPIO.HIGH)
         print ('DMP ...OFF')
         GPIO.output(5, GPIO.HIGH)
         print ('PMP 2 ...OFF')
         
         
        
         print ("end")
         GPIO.cleanup()        
       
        
 
       
            
     

        
            

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")
  GPIO.cleanup()

