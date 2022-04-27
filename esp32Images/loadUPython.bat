set COM="COM10"

esptool.py --chip esp32 --port %COM% erase_flash
esptool.py --chip esp32 --port %COM% --baud 460800 write_flash -z 0x1000 LAN_esp32-idf3-20190529-v1.11.bin
ampy --port %COM% --delay 1.0 reset
ampy --port %COM% run -n ..\ledTest.py