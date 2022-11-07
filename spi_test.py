#Author : Harindi Perera 
#date : 8/08 



from machine import Pin
import time

print("Conditions are a GO!")


#declaration

# Initialise the SPI bus 
spi = SPI(0, 10000000, sck=Pin(20), mosi=Pin(21), miso=Pin(22))

#Make sure CS is active high : if needing to do this in software - connect cs to a gpio on esp32 and do the following
# cs = Pin(4 , mode=Pin.OUT , value = 1)

#Initialise the bus
spi.init(baudrate=10000000)

#Comment Block out

# read 3 bytes on MISO
spi.read(3)

# read 3 bytes while outputting 0xff on MOSI
spi.read(3, 0xff)

#Create a buffer
buf = bytearray(10)

# read 10 bytes into the given buffer
spi.readinto(buf)

# read 10 bytes into the given buffer and output 0xff on mosi
spi.readinto(buf, 0xff)

# write specified buffer object on miso
spi.write(b"12345")

# create a buffer
buf = bytearray(5)

# write to MOSI and read from MISO into the buffer
spi.write_readinto(b"12345", buf)

# write buf to MOSI and read MISO back into buf
spi.write_readinto(buf, buf)

#close the bus
spi.deinit()