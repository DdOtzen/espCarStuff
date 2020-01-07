from machine import Pin
from time import sleep_ms, sleep

vf = Pin(15, Pin.OUT)
vb = Pin(4, Pin.OUT)

hb = Pin(5, Pin.OUT) 
hf = Pin(18, Pin.OUT)

led = Pin(2, Pin.OUT)

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
sleep_ms(300)

while True :
    frem()
    sleep_ms(500)
    bak()
    sleep_ms(500)
    drejH()
    sleep_ms(500)
    drejV()
    sleep_ms(500)
    roterH()
    sleep_ms(500)
    roterV()
    sleep_ms(500)
    coast()
