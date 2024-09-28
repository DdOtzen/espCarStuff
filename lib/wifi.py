from os import uname
from sys import implementation
import network
import ubinascii
import utime

from setup import ssid, password

wlan = 0

def init():
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

def connect():
    global wlan
    print('connect to network', ssid)
    
    wlan.active(True)
    if not wlan.isconnected():
        print('...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    
    print()
    print('network config:')
    print("interface's IP/netmask/gw/DNS addresses")
    print(wlan.ifconfig())
    
def scan():
    global wlan
    print('scan network...')
    wlan.active(True)
    for network in wlan.scan():
        print(network)
        

def print_sys_info():
    print(implementation.name)
    print(uname()[3])
    print(uname()[4])
    print()
