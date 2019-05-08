print('PMP 1 OFF')
from config import Color
from RPiSim import GPIO

#from EmulatorGUI import GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')
		return "asdf"

print(repr(Color.RED))

def my_callback(channel):  
        print ("tank "+str(channel)+" empty")
print(MyClass().func())
my_callback(1)
my_callback(1)
my_callback(1)