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


BLYNK_AUTH = 'O_yxfSKYV0U2hVvHqhGHGFCi5nlifPXC'
def connect():
    global blynk
    print("Connecting to Blynk...")
    blynk = BlynkLib.Blynk(BLYNK_AUTH)

    @blynk.on("connected")
    def blynk_connected(ping):
        print('Blynk ready. Ping:', ping, 'ms')

    return blynk


def runLoop():
    global blynk
    while True:
        blynk.run()
        machine.idle()

def limit( min, n, max):
    return sorted([min, n, max])[1]



