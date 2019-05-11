
from config import Switches, Buttons
from utils import safe_sleep

SleepTimeDELAY = 4
SleepTimeDMP = 180


def is_cancelled():
    return (not Buttons.is_started()) or (not Buttons.is_tank_2_empty_on())


def run_empty_tank_two():
    print("Start empty tank 2")

    Switches.pmp2.write_and_print(True)
    safe_sleep(SleepTimeDELAY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeDMP, is_cancelled)

    Switches.dump.write_and_print(False)
    Switches.pmp2.write_and_print(False)

    if not is_cancelled():
        print("🎉🎉 Tank 2 empty done")
