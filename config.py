from enum import IntEnum
import RPi.GPIO as GPIO


class Pins(IntEnum):
    TANK_1_DUMP = 19
    BUTTON_1 = 20
    BUTTON_2 = 21
    BUTTON_3 = 26
    START = 16


# Setup input and output
print("Configure GPIO")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup([Pins.TANK_1_DUMP, Pins.BUTTON_1, Pins.BUTTON_2,
            Pins.BUTTON_3, Pins.START], GPIO.IN, pull_up_down=GPIO.PUD_UP)
