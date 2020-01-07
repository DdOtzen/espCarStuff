from machine import Pin
from time import sleep_ms

led = Pin( 2, Pin.OUT )
count = 0
duty = 0
while True :
    if count == 100 :
        count = 0
        if duty == 10 :
            duty = 0
        else:
            duty += 1
        print( "on: {}, off {}".format( duty, 10 - duty ) )        
    else :
        count += 1
        
    led.on()
    sleep_ms( duty )
    led.off()
    sleep_ms( 10 - duty)
    