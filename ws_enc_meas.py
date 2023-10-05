"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows how to initialize your ESP8266/ESP32 board
and connect it to Blynk.

Don't forget to change WIFI_SSID, WIFI_PASS and BLYNK_AUTH ;)
"""

import BlynkLib
import network
import machine



#WIFI_SSID = 'Maolin'
#WIFI_PASS = 'WroomWroom'

WIFI_SSID = 'AlsLUG'
WIFI_PASS = 'TuxRocks'

BLYNK_AUTH = 'O_yxfSKYV0U2hVvHqhGHGFCi5nlifPXC'

print("Connecting to WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH)

motor_H = machine.Pin(2, machine.Pin.OUT)
motor_H.off()
motorPwm_H = machine.PWM( motor_H, freq=1000, duty=0 )
dir_H = machine.Pin(4, machine.Pin.OUT)

motor_V = machine.Pin(16, machine.Pin.OUT)
motorPwm_V = machine.PWM( motor_V, freq=1000, duty=0 )
dir_V = machine.Pin(17, machine.Pin.OUT)
speed = 0
direction = 0

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')
    

def runLoop():
    motor_H.off()
    motor_V.off()
    while True:
        blynk.run()
        machine.idle()

def limit( min, n, max):
    return sorted([min, n, max])[1]


def UpdateSpeed():
    print('Speed: {}    direction: {}'.format( speed, direction ) )
    speed_H = limit( -1023, speed - direction, 1023 ) 
    speed_V = limit( -1023, speed + direction, 1023 )
 
    print('Spped V: {}    Speed_H: {}'.format( speed_V, speed_H ) )
    
    if speed_V < 0:
        dir_V.on()
        motorPwm_V.duty( 1023 + speed_V )
    else:
        dir_V.off()
        motorPwm_V.duty( speed_V )


    if speed_H < 0:
        dir_H.on()
        motorPwm_V.duty( 1023 + speed_H )
    else:
        dir_H.off()
        motorPwm_H.duty( speed_H )

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    global speed
    speed= int(value[0] )
#    print('Current V0 value: {}'.format( intVal ) )

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    global direction
    direction = int(value[0] )
#    print('Current V1 value: {}'.format( intVal ) )
    UpdateSpeed()




# Run blynk in the main thread:
runLoop()

# Or, run blynk in a separate thread (unavailable for esp8266):
#import _thread
#_thread.stack_size(5*1024)
#_thread.start_new_thread(runLoop, ())


# Note:
# Threads are currently unavailable on some devices like esp8266
# ESP32_psRAM_LoBo has a bit different thread API:
# _thread.start_new_thread("Blynk", runLoop, ())
