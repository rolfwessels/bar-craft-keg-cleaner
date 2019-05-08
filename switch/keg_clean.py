from config import Switches, Buttons
from utils import safe_sleep

SleepTimeDELAY = 4
SleepTimeDMP = 60


def is_cancelled():
    return (not Buttons.is_started()) or (not Buttons.is_keg_clean_on())


def run_keg_clean():
    print("Start keg clean")

    Switches.air.write_and_print(True)
    safe_sleep(SleepTimeDELAY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeDMP, is_cancelled)

    print("🎉🎉 keg clean done")
    Switches.dump.write_and_print(False)
    Switches.air.write_and_print(False)
