from config import Switches, Buttons
from utils import safe_sleep, TimeT
import datetime

# First & Final rinse
SleepTimeDELAY = 6
SleepTimeDMP = 25
SleepTimeDMP2 = 9
SleepTimePRIME = 55
SleepTimeRUN = 25

# Sanatizer phase
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


def is_cancelled():
    return (not Buttons.is_started()) or (not Buttons.is_full_run_on())


def first_rince():
    Switches.pmp1.write_and_print(True)
    safe_sleep(SleepTimeDELAY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeDMP2, is_cancelled)
    Switches.dump.write_and_print(False)
    Switches.recirc_t1.write_and_print(True)
    safe_sleep(SleepTimeRUN, is_cancelled)
    Switches.pmp1.write_and_print(False)
    safe_sleep(SleepTimeDMP2, is_cancelled)
    Switches.valve_t1.write_and_print(True)
    safe_sleep(SleepTimePRIME, is_cancelled)
    Switches.valve_t1.write_and_print(False)
    safe_sleep(SleepTimeDMP, is_cancelled)
    Switches.recirc_t1.write_and_print(False)


def clearing():
    Switches.valve_t1.write_and_print(True)
    safe_sleep(SleepTimeCLRDLY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeCLRRUN, is_cancelled)
    Switches.valve_t1.write_and_print(False)
    safe_sleep(SleepTimeCLRPRIME, is_cancelled)
    Switches.dump.write_and_print(False)


def sanatizerPhase():
    Switches.pmp2.write_and_print(True)
    safe_sleep(SleepTimeSANDLY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeSANDMP, is_cancelled)
    Switches.dump.write_and_print(False)
    Switches.recirc_t2.write_and_print(True)
    safe_sleep(SleepTimeSANRUN, is_cancelled)
    Switches.pmp2.write_and_print(False)
    safe_sleep(SleepTimeSANDMP2, is_cancelled)
    Switches.valve_t1.write_and_print(True)
    safe_sleep(SleepTimeSANPRIME, is_cancelled)
    Switches.valve_t1.write_and_print(False)
    safe_sleep(SleepTimeSANDMP, is_cancelled)
    Switches.recirc_t2.write_and_print(False)


def final_rinse():
    Switches.pmp1.write_and_print(True)
    safe_sleep(SleepTimeDELAY, is_cancelled)
    Switches.dump.write_and_print(True)
    safe_sleep(SleepTimeDMP, is_cancelled)
    Switches.dump.write_and_print(False)
    Switches.recirc_t1.write_and_print(True)
    safe_sleep(SleepTimeRUN, is_cancelled)
    Switches.pmp1.write_and_print(False)
    safe_sleep(SleepTimeDMP2, is_cancelled)
    Switches.valve_t1.write_and_print(True)
    safe_sleep(SleepTimePRIME, is_cancelled)
    Switches.valve_t1.write_and_print(False)
    safe_sleep(SleepTimeDMP2, is_cancelled)
    Switches.recirc_t1.write_and_print(False)


def final_clean():
    clearing()


def run_and_wrap(stageName, function, totalTime=0):
    eta = datetime.datetime.now() + datetime.timedelta(0, totalTime)
    print('-------- '+stageName +
          ' Started [eta ' + eta.strftime("%H:%M")+'] --------')
    function()
    print('-------- '+stageName+' Done 🎉 --------')
    Switches.print_on()
    # print(TimeT.totalTime)
    # TimeT.totalTime = 0


def full_run():
    run_and_wrap("First Rinse", first_rince, 129)
    run_and_wrap("Clearing", clearing, 28)
    run_and_wrap("Sanatizer Phase", sanatizerPhase, 164)
    run_and_wrap("Clearing", clearing, 28)
    run_and_wrap("Final Rinse", final_rinse, 129)
    run_and_wrap("Final Clearing", final_clean, 28)


def run_full_run():
    run_and_wrap("Full run", full_run, 506)

    print("🎉🎉🎉🎉 full run done 🎉🎉🎉🎉🎉🎉")
