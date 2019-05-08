#!/usr/bin/python.
from config import Pins
from switch.tank_2_empty import empty_tank_two
import time
import sys

try:
    while True:
        print('------------------')
        print('Program ready.')
        Pins.print()
        print('Press button to start.')
        print('------------------')
        print('')

        while not Pins.is_started():
            Pins.read_all()
            time.sleep(0.5)
            pass

        print('Starting')

        if Pins.is_started() & (not Pins.tank_2_empty_button.is_on()):
            empty_tank_two()

        print('press [start_stop] to stop.')
        print("Done ✔️ 🎉🎉🎉🎉🎉 ")
        Pins.StartStop.set(False)


except KeyboardInterrupt:
    print('   💥  Stopping   💥')
    sys.exit
