from machine import Pin, ADC
from time import sleep_ms

sensor = ADC( Pin( 34 ) )

sensor.atten(ADC.ATTN_11DB) # Ignorer dette !!!!!!!!

vf = Pin( 15, Pin.OUT )
hf = Pin( 18, Pin.OUT )

while True :
    sensorVal = sensor.read()
    
    if sensorVal > 1000 :
        vf.on()
        hf.on()
    else :
        hf.off()
        vf.off()
    sleep_ms(300)