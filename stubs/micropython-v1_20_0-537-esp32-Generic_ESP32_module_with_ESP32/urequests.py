"""
Module: 'urequests' on micropython-v1.20.0-537-esp32-Generic_ESP32_module_with_ESP32
"""
# MCU: {'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_ESP32', 'family': 'micropython', 'build': '537', 'arch': 'xtensawin', 'ver': 'v1.20.0-537', 'cpu': 'ESP32'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

def request(*args, **kwargs) -> Incomplete:
    ...

def head(*args, **kwargs) -> Incomplete:
    ...

def post(*args, **kwargs) -> Incomplete:
    ...

def patch(*args, **kwargs) -> Incomplete:
    ...

def delete(*args, **kwargs) -> Incomplete:
    ...

def put(*args, **kwargs) -> Incomplete:
    ...

def get(*args, **kwargs) -> Incomplete:
    ...


class Response():
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content : Incomplete ## <class 'property'> = <property>
    text : Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

