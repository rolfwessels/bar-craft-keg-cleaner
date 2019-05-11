import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [2, 3, 4, 5, 6, 12, 13, 17]
"""
2-VALVE_T1
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


# First & Final rinse
SleepTimeDELAY = 6
SleepTimeDMP = 25
SleepTimeDMP2 = 9
SleepTimePRIME = 55
SleepTimeRUN = 25

# sanatizer phase
SleepTimeSANDLY = 4
SleepTimeSANDMP = 21
SleepTimeSANDMP2 = 8
SleepTimeSANPRIME = 50
SleepTimeSANRUN = 60

# Clearing
SleepTimeCLRDLY = 10
SleepTimeCLRPRIME = 6
SleepTimeCLRRUN = 12
SleepTimeCLRDMP = 10


try:

    for i in pinList:
        # FIRST RINSE

        print('First Rinse...')

        GPIO.output(13, GPIO.LOW)
        print('PUMP 1 ON...')
        time.sleep(SleepTimeDELAY)
        GPIO.output(3, GPIO.LOW)
        print('DMP ON...')
        time.sleep(SleepTimeDMP2)

        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')
        GPIO.output(17, GPIO.LOW)
        print('RECIRC 1 ON...')
        time.sleep(SleepTimeRUN)

        GPIO.output(13, GPIO.HIGH)
        print('PMP 1 ...OFF')
        time.sleep(SleepTimeDMP2)

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON...')
        time.sleep(SleepTimePRIME)
        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeDMP)

        GPIO.output(17, GPIO.HIGH)
        print('RECIRC 1 ...OFF')

        print('Frist Rinse COMPLETED')

        # CLearing

        print('Clearing...')

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON..')
        time.sleep(SleepTimeCLRDLY)

        GPIO.output(3, GPIO.LOW)
        print('DUMP ON...')
        time.sleep(SleepTimeCLRRUN)

        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeCLRPRIME)
        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')

        print('Clearing COMPLETED')

        # SANATIZERPHASE

        print('SANATIZER PHASE...')

        GPIO.output(5, GPIO.LOW)
        print('PUMP 2 ON...')
        time.sleep(SleepTimeSANDLY)

        GPIO.output(3, GPIO.LOW)
        print('DMP ON...')
        time.sleep(SleepTimeSANDMP)

        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')

        GPIO.output(6, GPIO.LOW)
        print('RECIRC 2 ON...')
        time.sleep(SleepTimeSANRUN)

        GPIO.output(5, GPIO.HIGH)
        print('PMP 2 ...OFF')
        time.sleep(SleepTimeSANDMP2)

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON...')
        time.sleep(SleepTimeSANPRIME)
        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeSANDMP)

        GPIO.output(6, GPIO.HIGH)
        print('RECIRC 2 ...OFF')

        print('SANATIZER PHASE COMPLETE')

        # CLearing

        print('Clearing...')

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON...')
        time.sleep(SleepTimeCLRDLY)

        GPIO.output(3, GPIO.LOW)
        print('DUMP ON...')
        time.sleep(SleepTimeCLRRUN)

        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeCLRPRIME)
        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')

        # FINAL RINSE

        print('FINAL Rinse...')

        GPIO.output(13, GPIO.LOW)
        print('PUMP 1 ON...')
        time.sleep(SleepTimeDELAY)
        GPIO.output(3, GPIO.LOW)
        print('DMP ON...')
        time.sleep(SleepTimeDMP)

        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')
        GPIO.output(17, GPIO.LOW)
        print('RECIRC 1 ON...')
        time.sleep(SleepTimeRUN)

        GPIO.output(13, GPIO.HIGH)
        print('PMP 1 ...OFF')
        time.sleep(SleepTimeDMP2)

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON...')
        time.sleep(SleepTimePRIME)
        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeDMP2)

        GPIO.output(17, GPIO.HIGH)
        print('RECIRC 1 ...OFF')

        print('FINAL Rinse COMPLETED')

        # CLearing

        print('Clearing...')

        GPIO.output(4, GPIO.LOW)
        print('VALVE_T1 ON...')
        time.sleep(SleepTimeCLRDLY)

        GPIO.output(3, GPIO.LOW)
        print('DUMP ON...')
        time.sleep(SleepTimeCLRRUN)

        GPIO.output(4, GPIO.HIGH)
        print('VALVE_T1 ...OFF')
        time.sleep(SleepTimeCLRPRIME)
        GPIO.output(3, GPIO.HIGH)
        print('DMP ...OFF')

        print('KEG CLEAN')

        print("end")
        print(GPIO.input(13))
        print(GPIO.input(3))
        print(GPIO.input(17))

        print("end")
        GPIO.cleanup()


# End program cleanly with keyboard
except KeyboardInterrupt:
    print("  Quit")
