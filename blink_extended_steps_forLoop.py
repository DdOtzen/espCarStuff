from machine import Pin
from time import sleep_ms

led = Pin( 2, Pin.OUT )
duty = 0
while True :
    print( "on: {}, off {}".format( duty, 10 - duty ) )        
    for _ in range( 100 ) :
        led.on()
        sleep_ms( duty )
        led.off()
        sleep_ms( 10 - duty)
    
    if duty == 10 :
        duty = 0
    else:
        duty += 1
        
    