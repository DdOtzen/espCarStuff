from machine import Pin, PWM
from time import sleep_ms, sleep
from lib.car import Car

L_IN1 = Pin(25, Pin.OUT)
L_IN2 = Pin(26, Pin.OUT)
L_PWM = PWM(Pin(27), freq = 1000, duty = 0)

L_IN1.on()
L_IN2.off()
L_PWM.duty(500)

sleep(2)

L_PWM.duty(0)

L_IN1.off()
L_IN2.on()
L_PWM.duty(1000)

sleep(2)

L_PWM.duty(0)
