
# led = Pin(2, Pin.OUT)

from lib import wifi #set password in setup.py file
from lib import blynk
from lib.car import Car

wifi.print_sys_info()
wifi.init()
wifi.scan()
wifi.connect()

phone = blynk.connect()
bil = Car()
# Register Virtual Pins

@phone.VIRTUAL_WRITE(5)
def my_write_handler(value):
    intVal = int(value[0] )
    print('Current V5 value: {}'.format( intVal ) )
    bil.coast()

@phone.VIRTUAL_WRITE(8)
def my_write_handler(value):
    intVal = int(value[0] )
    print('Current V8 value: {}'.format( intVal ) )
    bil.frem()
    
@phone.VIRTUAL_WRITE(20)
def my_write_handler(value):
    fart = int(value[0] )
    print('Current V20 value: {}'.format( fart ) )
    bil.set_fart(fart)



# Run blynk in the main thread:
blynk.runLoop()

