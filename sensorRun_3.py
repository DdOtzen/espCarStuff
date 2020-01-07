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
def coast() :
    hf.off()
    vf.off()
    hb.off()
    vb.off()
    
def frem() :
    print( 'frem')
    vf.on()
    hf.on()
    vb.off()
    hb.off()


def bak() :
    coast()
    vb.on()
    hb.on()

def drejH() :
    coast()
    vf.on()

def drejV() :
    coast()
    hf.on()

def roterH() :
    print( 'roterH')
    vf.on()
    vb.off()
    hf.off()
    hb.on()
    

def roterV() :
    coast()
    hf.on()
    vb.on()

led.on()
sleep_ms(300)
led.off()

fremad = True
while True :
    dist = sensor.read()
    print( dist )
    
    if fremad :
        if dist > 2000 :
            roterH()
    else :
        if dist < 2500  :
            frem()

    sleep_ms(10)
    
    