from machine import Pin, PWM

led_pin = Pin( 2 )
led = PWM( led_pin )
led.freq(10)
led.duty( 512 )
