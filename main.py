
from config import Pins
import time
import sys


# class MyClass:
#     "This is my second class"
#     a = 10

#     def func(self):
#         print('Hello')
#         return "asdf"


# def my_callback(channel):
#     print("tank "+str(channel)+" empty")


# print(MyClass().func())
# my_callback(1)

try:
    while True:
        print('------------------')
        print('Program ready.')
        Pins.print()
        print('Press button to start.')
        print('------------------')
        print('')

        while not Pins.is_started():
            time.sleep(0.5)
            pass

        print('Starting')
        print('press [start_stop] to stop.')
        print("  Done   ")
        Pins._startStop = False


except KeyboardInterrupt:
    print('Stopping')
    sys.exit
