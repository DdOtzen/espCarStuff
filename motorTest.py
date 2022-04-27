from machine import Pin
from time import sleep_ms, sleep
from lib.car import Car

led = Pin(2, Pin.OUT)
bil = Car()



led.on()
while True:
    sleep(5)

    #blinke
    for _ in range(7):
        led.on()
        sleep_ms(300)
        led.off()
        sleep_ms(300)


    bil.set_fart(100)

    bil.frem()
    sleep_ms(500)

    bil.bak()
    sleep_ms(500)

    bil.drejH()
    sleep_ms(500)

    bil.drejV()
    sleep_ms(500)

    bil.roterH()
    sleep_ms(1000)

    bil.roterV()
    sleep_ms(1000)

    bil.coast()
