from config import Config
import time
import datetime


class TimeT:
    totalTime = 0


def safe_sleep(delay, is_cancelled):
    if is_cancelled():
        return
    stop_time = datetime.datetime.now() + datetime.timedelta(0, delay)
    if (delay > 60):
        print("sleeping "+str(delay)+"s eta", stop_time.strftime("%H:%M"))
    else:
        print("💤  "+str(delay)+"s ")

    TimeT.totalTime += delay
    if Config.is_dry_run:
        stop_time = datetime.datetime.now() + datetime.timedelta(0, 1)
    while (datetime.datetime.now() < stop_time) and (not is_cancelled()):
        time.sleep(0.5)
    if (datetime.datetime.now() < stop_time):
        print('')
        print('🛑    Stopping !!')
        print('')
