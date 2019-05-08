
import RPi.GPIO as GPIO
import time
import sys 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [2, 3, 4, 5, 6, 12, 13, 17]
"""
2-Air
3-DUMP
4-Valve T1
5-PMP2
6-RECIRC T2
12-VALVE T2
13-PMP1
17-RECIRC T1
"""

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)
     

SleepTimeDELAY = 2
SleepTimeDMP = 21
SleepTimeDMP2 = 29

SleepTimePRIME = 20
SleepTimeRUN = 8


try:
    
    for i in pinList:
         GPIO.output(13, GPIO.LOW)
         print ('PUMP 1 ON') 
         time.sleep(SleepTimeDELAY);
         GPIO.output(3, GPIO.LOW)
         print ('DMP ON')
         time.sleep(SleepTimeDMP);
         
         GPIO.output(3, GPIO.HIGH)
         print ('DMP OFF')
         GPIO.output(17, GPIO.LOW)
         print ('RECIRC 1 ON')
         time.sleep(SleepTimeRUN);
         
         
         GPIO.output(13, GPIO.HIGH)
         print ('PMP 1 OFF')
         time.sleep(SleepTimeDMP2);
         
         GPIO.output(2, GPIO.LOW)
         print ('AIR ON')
         time.sleep(SleepTimePRIME);
         GPIO.output(2, GPIO.HIGH)
         print ('AIR OFF')
         time.sleep(SleepTimeDMP2);

                 
         GPIO.output(17, GPIO.HIGH)
         print ('RECIRC 1 OFF')
         
    
                 
         
 
         print ("end")
         print (GPIO.input(13))
         print (GPIO.input(3))
         print (GPIO.input(17))
         sys.exit()          
    
   
        
         

 
    

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
GPIO.cleanup()
         
         


         
         
         
