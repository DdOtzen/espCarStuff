from machine import Pin, ADC, PWM
from time import sleep_ms, sleep

vf = Pin(17, Pin.OUT)
vb = Pin(4, Pin.OUT)

hb = Pin(16, Pin.OUT) 
hf = Pin(15, Pin.OUT)

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
    coast()
    vf.on()
    hf.on()

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
    coast()
    vf.on()
    hb.on()

def roterV() :
    coast()
    hf.on()
    vb.on()

led.on()
sleep_ms(300)
led.off()
while True :
    frem()
    while( sensor.read() < 1000 ) :
        sleep_ms(1)
    coast()
    sleep_ms(500)

    roterH()
    while( sensor.read() > 800 ) :
        sleep_ms(1)
    coast()
    sleep_ms(500)
    
    