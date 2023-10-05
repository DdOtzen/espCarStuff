"""
Module: 'ussl' on micropython-v1.20.0-537-esp32-Generic_ESP32_module_with_ESP32
"""
# MCU: {'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_ESP32', 'family': 'micropython', 'build': '537', 'arch': 'xtensawin', 'ver': 'v1.20.0-537', 'cpu': 'ESP32'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

CERT_REQUIRED = 2 # type: int
PROTOCOL_TLS_CLIENT = 0 # type: int
PROTOCOL_TLS_SERVER = 1 # type: int
CERT_OPTIONAL = 1 # type: int
CERT_NONE = 0 # type: int
def wrap_socket(*args, **kwargs) -> Incomplete:
    ...


class SSLContext():
    def wrap_socket(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

