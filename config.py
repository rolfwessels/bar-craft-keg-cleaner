import RPi.GPIO as GPIO
from pins import PinInstance
from pins import PinInstanceInverse


class Config:
    is_dry_run = False


class Buttons:
    full_run = PinInstance("Full Run", 19, False)
    tank_1_empty = PinInstance("Tank 1 Empty", 20, False)
    tank_2_empty = PinInstance("Tank 2 Empty", 21, False)
    keg_clean = PinInstance("Keg Clean", 26, False)
    start_stop = PinInstance("Started ", 16, False)

    @staticmethod
    def all_pins():
        return [Buttons.full_run, Buttons.tank_1_empty, Buttons.tank_2_empty, Buttons.keg_clean, Buttons.start_stop]

    @staticmethod
    def read_all():
        for value in Buttons.all_pins():
            if value != Buttons.start_stop:
                value.set_and_print(value.read())

    @staticmethod
    def is_full_run_on():
        if not Config.is_dry_run:
            Buttons.full_run.set_and_print(Buttons.full_run.read())
        return Buttons.full_run.is_on()

    @staticmethod
    def is_tank_1_empty_on():
        if not Config.is_dry_run:
            Buttons.tank_1_empty.set_and_print(Buttons.tank_1_empty.read())
        return Buttons.tank_1_empty.is_on()

    @staticmethod
    def is_tank_2_empty_on():
        if not Config.is_dry_run:
            Buttons.tank_2_empty.set_and_print(Buttons.tank_2_empty.read())
        return Buttons.tank_2_empty.is_on()

    @staticmethod
    def is_keg_clean_on():
        if not Config.is_dry_run:
            Buttons.keg_clean.set_and_print(Buttons.keg_clean.read())
        return Buttons.keg_clean.is_on()

    @staticmethod
    def is_started():
        return Buttons.start_stop.is_on()

    @staticmethod
    def start_stop_click(channel):
        Buttons.start_stop.set_and_print(not Buttons.start_stop.is_on())

    @staticmethod
    def print():
        for value in Buttons.all_pins():
            value.print()


class Switches:

    air = PinInstanceInverse("Air    ", 2, False)
    dump = PinInstanceInverse("Dump   ", 3, False)
    valve_t1 = PinInstanceInverse("Valve T1", 4, False)
    pmp2 = PinInstanceInverse("Pump 2", 5, False)
    recirc_t2 = PinInstanceInverse("Recirc T2", 6, False)
    valve_t2 = PinInstanceInverse("Valve T2", 12, False)
    pmp1 = PinInstanceInverse("Pump 1  ", 13, False)
    recirc_t1 = PinInstanceInverse("Recirc T1", 17, False)

    @staticmethod
    def all_pins():
        return [Switches.air,
                Switches.dump,
                Switches.valve_t1,
                Switches.pmp2,
                Switches.recirc_t2,
                Switches.valve_t2,
                Switches.pmp1,
                Switches.recirc_t1]

    @staticmethod
    def read_all():
        for value in Switches.all_pins():
            value.set_and_print(value.read())

    @staticmethod
    def write_all():
        for value in Switches.all_pins():
            value.write()

    @staticmethod
    def print_on():
        for value in Switches.all_pins():
            if value.is_on():
                value.print()

    @staticmethod
    def reset_all():
        for value in Switches.all_pins():
            value.write_and_print(False)


def read_and_print_pins(channel):
    Buttons.print()


# Setup input and output
print("Configure all GPIO inputs and outputs")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup([Buttons.full_run.pin(), Buttons.tank_1_empty.pin(), Buttons.tank_2_empty.pin(),
            Buttons.keg_clean.pin(), Buttons.start_stop.pin()], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

all_pins = list(map(lambda x: x.pin(), Switches.all_pins()))
GPIO.setup(all_pins, GPIO.OUT)


GPIO.add_event_detect(Buttons.start_stop.pin(), GPIO.FALLING,
                      callback=Buttons.start_stop_click, bouncetime=300)
print("Read buttons and set switches to defaults")
Buttons.read_all()
Switches.write_all()
