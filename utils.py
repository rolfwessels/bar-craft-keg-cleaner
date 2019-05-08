import RPi.GPIO as GPIO
import time
import datetime


class PinInstance:
    _onOff = False
    _name = ""
    _pin = 0

    def __init__(self, name, pin, state):
        self._name = name
        self._pin = pin
        self._onOff = state

    def set(self, value):
        self._onOff = value

    def read(self):
        return GPIO.input(self._pin) == GPIO.HIGH

    def write(self):
        # print("settings", self._pin, self._name, self.get_pin_voltage())
        return GPIO.output(self._pin, self.get_pin_voltage())

    def get_pin_voltage(self):
        return GPIO.HIGH if self._onOff else GPIO.LOW

    def pin(self):
        return self._pin

    def is_on(self):
        return self._onOff

    def print(self):
        print(self._name, "\t\t", "🔵" if (self._onOff) else "⚪")

    def write_and_print(self, value):
        if (self._onOff != value):
            self._onOff = value
            self.print()
        self.write()

    def set_and_print(self, value):
        if (self._onOff != value):
            self._onOff = value
            self.print()


class PinInstanceInverse(PinInstance):
    def get_pin_voltage(self):
        return GPIO.LOW if self._onOff else GPIO.HIGH


def safe_sleep(delay, is_cancelled):
    stop_time = datetime.datetime.now() + datetime.timedelta(0, delay)
    print("sleeping "+str(delay)+"s eta", stop_time.time())
    stop_time = datetime.datetime.now() + datetime.timedelta(0, 5)
    while (datetime.datetime.now() < stop_time) and (not is_cancelled()):
        time.sleep(0.5)
