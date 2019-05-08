#!/usr/bin/python.
from config import Buttons
from switch.tank_2_empty import run_empty_tank_two
from switch.tank_1_empty import run_empty_tank_one
import time
import sys
Buttons.start_stop.set(True)
Buttons.tank_2_empty.set(True)
Buttons.tank_1_empty.set(True)
try:
    while True:
        print('------------------')
        print('Program ready.')
        Buttons.print()
        print('Press button to start.')
        print('------------------')
        print('')

        while not Buttons.is_started():
            Buttons.read_all()
            time.sleep(0.5)
            pass

        print('Starting')

        if Buttons.is_started() & (Buttons.is_tank_1_empty_on()):
            run_empty_tank_one()

        if Buttons.is_started() & (Buttons.is_tank_2_empty_on()):
            run_empty_tank_two()

        print('press [start_stop] to stop.')
        Buttons.start_stop.set(False)


except KeyboardInterrupt:
    print('   💥  Stopping   💥')
    sys.exit
