from machine import UART

uart = UART(1,115200)
uart.init(baudrate = 115200, bits=8, parity=None, stop=1)

reply = b'\x01\x00'

while True:
    msg = uart.read()

    if msg:
        if msg == b'\x00\x01':
            uart.write(reply)