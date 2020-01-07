from machine import Pin
import time

switch = Pin(34, Pin.IN )

while True :
    print( switch.value() )
    time.sleep_ms(500)
