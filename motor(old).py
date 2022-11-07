from machine import Pin
import os
from time import sleep_us

step = 0

# Changes the direction of the pin motor
mot_dir = Pin(25, Pin.OUT)
mot_dir.off()


# Motor movement - pulse with timing between pulses controlling speed
mot_stp = Pin(33, Pin.OUT)
while True:
    
    mot_stp.on()
    print("on")
    sleep_us(1000)
    mot_stp.off()
    print("off")
    sleep_us(1000)
  
    

