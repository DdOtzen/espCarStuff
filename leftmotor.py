from machine import Pin
import time

len = Pin(27, Pin.OUT)
lin1 = Pin(25, Pin.OUT)
lin2 = Pin(26, Pin.OUT)

lin1.on()
lin2.off()

while(1):
    lin1.on()
    lin2.off()
    len.on()
    time.sleep(2)
    len.off()
    time.sleep(2)

    lin1.off()
    lin2.on()
    len.on()
    time.sleep(2)
    len.off()
    time.sleep(2)
