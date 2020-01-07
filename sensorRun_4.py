from machine import Pin, ADC, PWM
from time import sleep_ms, sleep

vf = Pin(15, Pin.OUT)
vb = Pin(4, Pin.OUT)

hb = Pin(5, Pin.OUT) 
hf = Pin(18, Pin.OUT)

led = Pin(2, Pin.OUT)
sensor = ADC( Pin(34 ))

led.on()
sleep_ms(300)
led.off()
sleep_ms(300)

led.on()
sleep_ms(300)
led.off()

fremad = True
while True :
    dist = sensor.read()
    print( dist )
    
    if fremad :
        if dist > 2000 :
            vf.on()
            vb.off()
            hf.off()
            hb.on()
    else :
        if dist < 2500  :
            vf.on()
            hf.on()
            vb.off()
            hb.off()

    sleep_ms(10)
    
    