set COM="COM6"

esptool --chip esp32 --port %COM% erase_flash
esptool --chip esp32 --port %COM% --baud 460800 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
ampy --port %COM% --delay 1.0 reset
ampy --port %COM% run -n ..\ledTest.py