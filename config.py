import RPi.GPIO as GPIO


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
        return GPIO.input(self._pin) == 1

    def pin(self):
        return self._pin

    def is_on(self):
        return self._onOff

    def print(self):
        print(self._name, "\t\t", "🔵" if (self._onOff) else "⚪")

    def set_and_print(self, value):
        if (self._onOff != value):
            self._onOff = value
            self.print()


class Pins:
    FullRun = PinInstance("Full Run", 19, False)
    Tank1Empty = PinInstance("Tank 1 Empty", 20, False)
    tank_2_empty_button = PinInstance("Tank 2 Empty", 21, False)
    KegEmpty = PinInstance("Keg Empty", 26, False)
    StartStop = PinInstance("Started ", 16, False)

    @staticmethod
    def all_pins():
        return [Pins.FullRun, Pins.Tank1Empty, Pins.tank_2_empty_button, Pins.KegEmpty, Pins.StartStop]

    @staticmethod
    def read_all():
        for value in Pins.all_pins():
            if value != Pins.StartStop:
                value.set_and_print(value.read())

    @staticmethod
    def is_fullRun_on():
        return Pins.FullRun.is_on()

    @staticmethod
    def is_tank1Empty_on():
        return Pins.Tank1Empty.is_on()

    @staticmethod
    def is_tank2Empty_on():
        return Pins.tank_2_empty_button.is_on()

    @staticmethod
    def is_kegEmpty_on():
        return Pins.KegEmpty.is_on()

    @staticmethod
    def is_started():
        return Pins.StartStop.is_on()

    @staticmethod
    def start_stop_click(channel):
        Pins.StartStop.set_and_print(not Pins.StartStop.is_on())

    @staticmethod
    def print():
        for value in Pins.all_pins():
            value.print()


def read_and_print_pins(channel):
    Pins.print()


# Setup input and output
print("Configure GPIO")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup([Pins.FullRun.pin(), Pins.Tank1Empty.pin(), Pins.tank_2_empty_button.pin(),
            Pins.KegEmpty.pin(), Pins.StartStop.pin()], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(Pins.StartStop.pin(), GPIO.FALLING,
                      callback=Pins.start_stop_click, bouncetime=300)

Pins.read_all()
