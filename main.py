#!/usr/bin/python.
from config import Buttons
from switch.tank_2_empty import run_empty_tank_two
from switch.tank_1_empty import run_empty_tank_one
from switch.keg_clean import run_keg_clean
from switch.full_run import run_full_run
import time
import sys

Buttons.start_stop.set_and_print(True)
Buttons.full_run.set_and_print(True)

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

        if Buttons.is_started() & (Buttons.is_keg_clean_on()):
            run_keg_clean()

        if Buttons.is_started() & (Buttons.is_full_run_on()):
            run_full_run()

        print('press [start_stop] to stop.')
        Buttons.start_stop.set(False)


except KeyboardInterrupt:
    print('   💥  Stopping   💥')
    sys.exit
