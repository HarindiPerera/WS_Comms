from machine import UART

uart = UART(baudrate = 115200, bits=8, parity=None, stop=1, tx=1, rx=3)

reply = b'\x01\x00'

while true:
    msg = uart.read()

    if msg:
        if msg == b'\x00\x01':
            uart.write(reply)