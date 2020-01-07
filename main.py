from machine import Pin, PWM
import math
import time

led_pin = Pin( 2 )
led = PWM( led_pin )
led.freq(1000)
wait = 100
wait_blink = 100

led.duty(1023)
time.sleep_ms( wait_blink )
led.duty(0)
time.sleep_ms( wait_blink )
led.duty(1023)
time.sleep_ms( wait_blink )
led.duty(0)
time.sleep_ms( wait_blink )
led.duty(0)
time.sleep_ms( wait_blink )
led.duty(1023)
time.sleep_ms( wait_blink )

while True :
    for i in range(40):
        duty = int( math.sin( i / 20 * math.pi) * 512 + 512 - 0.5 )
        #print( duty )
        led.duty( duty )
        time.sleep_ms( wait )
