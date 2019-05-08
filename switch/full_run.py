from config import Switches, Buttons
from utils import safe_sleep

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


def run_full_run():
    print("Start full run")

    # FIRST RINSE

    print('-------- First Rinse --------')

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

    print('-------- First Rinse Done 🎉 --------')

    # CLearing
    print('-------- Clearing --------')
    # print('Clearing...')

    # GPIO.output(4, GPIO.LOW)
    # print('AIR ON..')
    # safe_sleep(SleepTimeCLRDLY, is_cancelled)

    # GPIO.output(3, GPIO.LOW)
    # print('DUMP ON...')
    # safe_sleep(SleepTimeCLRRUN, is_cancelled)

    # GPIO.output(4, GPIO.HIGH)
    # print('AIR ...OFF')
    # safe_sleep(SleepTimeCLRPRIME, is_cancelled)
    # GPIO.output(3, GPIO.HIGH)
    # print('DMP ...OFF')

    # print('Clearing COMPLETED')

    # # SANATIZERPHASE

    # print('SANATIZER PHASE...')

    # GPIO.output(5, GPIO.LOW)
    # print('PUMP 2 ON...')
    # safe_sleep(SleepTimeSANDLY, is_cancelled)

    # GPIO.output(3, GPIO.LOW)
    # print('DMP ON...')
    # safe_sleep(SleepTimeSANDMP, is_cancelled)

    # GPIO.output(3, GPIO.HIGH)
    # print('DMP ...OFF')

    # GPIO.output(6, GPIO.LOW)
    # print('RECIRC 2 ON...')
    # safe_sleep(SleepTimeSANRUN, is_cancelled)

    # GPIO.output(5, GPIO.HIGH)
    # print('PMP 2 ...OFF')
    # safe_sleep(SleepTimeSANDMP2, is_cancelled)

    # GPIO.output(4, GPIO.LOW)
    # print('AIR ON...')
    # safe_sleep(SleepTimeSANPRIME, is_cancelled)
    # GPIO.output(4, GPIO.HIGH)
    # print('AIR ...OFF')
    # safe_sleep(SleepTimeSANDMP, is_cancelled)

    # GPIO.output(6, GPIO.HIGH)
    # print('RECIRC 2 ...OFF')

    # print('SANATIZER PHASE COMPLETE')

    # # CLearing

    # print('Clearing...')

    # GPIO.output(4, GPIO.LOW)
    # print('AIR ON...')
    # safe_sleep(SleepTimeCLRDLY, is_cancelled)

    # GPIO.output(3, GPIO.LOW)
    # print('DUMP ON...')
    # safe_sleep(SleepTimeCLRRUN, is_cancelled)

    # GPIO.output(4, GPIO.HIGH)
    # print('AIR ...OFF')
    # safe_sleep(SleepTimeCLRPRIME, is_cancelled)
    # GPIO.output(3, GPIO.HIGH)
    # print('DMP ...OFF')

    # # FINAL RINSE

    # print('FINAL Rinse...')

    # GPIO.output(13, GPIO.LOW)
    # print('PUMP 1 ON...')
    # safe_sleep(SleepTimeDELAY, is_cancelled)
    # GPIO.output(3, GPIO.LOW)
    # print('DMP ON...')
    # safe_sleep(SleepTimeDMP, is_cancelled)

    # GPIO.output(3, GPIO.HIGH)
    # print('DMP ...OFF')
    # GPIO.output(17, GPIO.LOW)
    # print('RECIRC 1 ON...')
    # safe_sleep(SleepTimeRUN, is_cancelled)

    # GPIO.output(13, GPIO.HIGH)
    # print('PMP 1 ...OFF')
    # safe_sleep(SleepTimeDMP2, is_cancelled)

    # GPIO.output(4, GPIO.LOW)
    # print('AIR ON...')
    # safe_sleep(SleepTimePRIME, is_cancelled)
    # GPIO.output(4, GPIO.HIGH)
    # print('AIR ...OFF')
    # safe_sleep(SleepTimeDMP2, is_cancelled)

    # GPIO.output(17, GPIO.HIGH)
    # print('RECIRC 1 ...OFF')

    # print('FINAL Rinse COMPLETED')

    # # CLearing

    # print('Clearing...')

    # GPIO.output(4, GPIO.LOW)
    # print('AIR ON...')
    # safe_sleep(SleepTimeCLRDLY, is_cancelled)

    # GPIO.output(3, GPIO.LOW)
    # print('DUMP ON...')
    # safe_sleep(SleepTimeCLRRUN, is_cancelled)

    # GPIO.output(4, GPIO.HIGH)
    # print('AIR ...OFF')
    # safe_sleep(SleepTimeCLRPRIME, is_cancelled)
    # GPIO.output(3, GPIO.HIGH)
    # print('DMP ...OFF')

    # print('KEG CLEAN')

    print("🎉🎉 full run done")
    Switches.dump.write_and_print(False)
    Switches.air.write_and_print(False)
    Switches.print_on()
