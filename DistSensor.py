from machine import Pin, ADC
from time import sleep_ms

sensor = ADC( Pin(34 ) )
sensor.atten(ADC.ATTN_11DB)

while True:
    v1 = sensor.read()
    sleep_ms( 30 )
    v2 = sensor.read()
    sleep_ms( 30 )
    v3 = sensor.read()
    sleep_ms( 30 )
    v4 = sensor.read()
    sleep_ms( 30 )
    v5 = sensor.read()
    sleep_ms( 30 )
    print( int( ( v1 + v2 + v3 + v4 + v5 ) / 5 ) )
    sleep_ms( 300 )
    