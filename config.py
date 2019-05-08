import RPi.GPIO as GPIO


class Pins:
    FullRun = 19
    Tank1Empty = 20
    Tank2Empty = 21
    KegEmpty = 26
    StartStop = 16

    _fullRun = False
    _tank1Empty = False
    _tank2Empty = False
    _kegEmpty = False
    _startStop = False

    @staticmethod
    def all_pins():
        return {"Fullrun": Pins._fullRun,
                "Tank 1 Empty": Pins._tank1Empty,
                "Tank 2 Empty": Pins._tank2Empty,
                "Keg Empty": Pins._kegEmpty,
                "Start": Pins._startStop}

    @staticmethod
    def read_all():
        Pins._fullRun = GPIO.input(Pins.FullRun) == 1
        Pins._tank1Empty = GPIO.input(Pins.Tank1Empty) == 1
        Pins._tank2Empty = GPIO.input(Pins.Tank2Empty) == 1
        Pins._kegEmpty = GPIO.input(Pins.KegEmpty) == 1
        Pins._startStop = GPIO.input(Pins.StartStop) == 1

    @staticmethod
    def is_fullRun_enabled():
        return Pins._fullRun
    @staticmethod
    def is_tank1Empty_enabled():
        return Pins._tank1Empty
    @staticmethod
    def is_tank2Empty_enabled():
        return Pins._tank2Empty
    @staticmethod
    def is_kegEmpty_enabled():
        return Pins._kegEmpty
    @staticmethod
    def is_started():
        return Pins._startStop


    @staticmethod
    def get_fullRun():
        return Pins._fullRun

    @staticmethod
    def start_stop_click(channel):
        Pins._startStop = not Pins._startStop
        print("Start", "[on]" if (Pins._startStop == 1)else "[off]")

    @staticmethod
    def print():
        for key, value in Pins.all_pins().items():
            print(key, "[on]" if value else "[off]")


# Setup input and output
print("Configure GPIO")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup([Pins.FullRun, Pins.Tank1Empty, Pins.Tank2Empty,
            Pins.KegEmpty, Pins.StartStop], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(Pins.StartStop, GPIO.FALLING,
                      callback=Pins.start_stop_click, bouncetime=300)
Pins.read_all()


# GPIO.add_event_detect([Pins.FullRun, Pins.Tank1Empty, Pins.Tank2Empty,
#                        Pins.KegEmpty, Pins.StartStop], GPIO.FALLING, callback=Pins.read_all, bouncetime=300)
