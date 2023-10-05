"""
Module: 'ubluetooth' on micropython-v1.20.0-537-esp32-Generic_ESP32_module_with_ESP32
"""
# MCU: {'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_ESP32', 'family': 'micropython', 'build': '537', 'arch': 'xtensawin', 'ver': 'v1.20.0-537', 'cpu': 'ESP32'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

FLAG_NOTIFY = 16 # type: int
FLAG_READ = 2 # type: int
FLAG_WRITE = 8 # type: int
FLAG_INDICATE = 32 # type: int
FLAG_WRITE_NO_RESPONSE = 4 # type: int

class UUID():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class BLE():
    def gattc_write(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_indicate(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_services(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_read(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_exchange_mtu(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_set_buffer(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_write(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_notify(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_register_services(self, *args, **kwargs) -> Incomplete:
        ...

    def gatts_read(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_advertise(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_connect(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_descriptors(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_scan(self, *args, **kwargs) -> Incomplete:
        ...

    def gattc_discover_characteristics(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_passkey(self, *args, **kwargs) -> Incomplete:
        ...

    def gap_pair(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

