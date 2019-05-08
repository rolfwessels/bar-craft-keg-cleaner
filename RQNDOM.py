def my_callback(channel):  
    print "falling edge detected on 17"  
  
def my_callback2(channel):  
    print "falling edge detected on 23"  
  
print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"  
print "You will also need a second button connected so that when pressed"  
print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)\n"  
print "You will also need a third button connected so that when pressed"  
print "it will connect GPIO port 17 (pin 11) to GND (pin 14)"  
raw_input("Press Enter when ready\n>")  
  
# when a falling edge is detected on port 17, regardless of whatever   
# else is happening in the program, the function my_callback will be run  
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  
  
# when a falling edge is detected on port 23, regardless of whatever   
# else is happening in the program, the function my_callback2 will be run  
# 'bouncetime=300' includes the bounce control written into interrupts2a.py  
GPIO.add_event_detect(23, GPIO.FALLING, callback=my_callback2, bouncetime=300)  
  
try:  
    print "Waiting for rising edge on port 24"  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print "Rising edge detected on port 24. Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
