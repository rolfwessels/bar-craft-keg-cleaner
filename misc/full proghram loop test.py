#!/usr/bin/env python
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#buttons
TANK_1_DUMP=[19]
BUTTON_1 = [20]
BUTTON_2 = [21]
BUTTON_3 = [26]
START = [16]

GPIO.setup(TANK_1_DUMP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_1 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_3 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(START , GPIO.IN, pull_up_down=GPIO.PUD_UP)


#PIN Status
print (GPIO.input(19))
print (GPIO.input(20))
print (GPIO.input(21))
print (GPIO.input(26))
print (GPIO.input(16))

if True:
    run=0
    GPIO.wait_for_edge(16, GPIO.FALLING)
    
    print ('Program ready')
    
    def my_callback(channel):  
        print ("tank 2 empty")
        run = 0
        while True :
                
                   print ("  Started TANK_2_empty")
                   import TANK_2_empty
                
                   run=0
                   while GPIO.input(21)==1:
                         time.sleep(0.01)

    def my_callback2(channel):  
        print ("tank 1 empty")
        run = 0
        while True :
                
                   print ("  Started TANK_1_empty")
                   import TANK_1_empty
                
                   run=1
                   while GPIO.input(20)==1:
                      time.sleep(0.01)
        
                       
    def my_callback3(channel):  
        print ("fULL rUN")
        run = 0
        while True :
                
                   print ("  Started fULL RUUN")
                   import Fullrun
                
                   run=1
                   
                   while GPIO.input(19)==1:
                         time.sleep(0.01)
                       
    def my_callback4(channel):  
        print ("Keg EMPTY")
        run = 0
        while True :
                
                   print ("  Started Keg empty")
                   import Kegclear
                
                   run=1
                   while GPIO.input(26)==1:
                         time.sleep(0.01)               
                   
GPIO.add_event_detect(21, GPIO.FALLING, callback=my_callback, bouncetime=300)
GPIO.add_event_detect(20, GPIO.FALLING, callback=my_callback2, bouncetime=300)
GPIO.add_event_detect(19, GPIO.FALLING, callback=my_callback3, bouncetime=300)
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback4, bouncetime=300)




# when a falling edge is detected on port 23, regardless of whatever   
# else is happening in the program, the function my_callback2 will be run  
# 'bouncetime=300' includes the bounce control written into interrupts2a.py  


try:
    GPIO.setmode(GPIO.BCM)

    run = 0
    
    while True :
        
          
        
       
        GPIO.wait_for_edge(16, GPIO.RISING)  
        print ('press exit to stop ')        
        if GPIO.input(16) ==0 and run == 0:
            print ("  QUIT   ")
            GPIO.cleanup()
           
            
            
        
                
          
                
        
                
                
        

except KeyboardInterrupt:
    print('Emergency STOP')
    GPIO.cleanup()
    sys.exit


GPIO.cleanup()