from machine import Pin
import os
from time import sleep_us

step = 0

#E
mot_vm_en = Pin(32 , Pin.OUT)
mot_vm_en.on()

mot_m_en = Pin(27 , Pin.OUT)
mot_m_en.on()

# Changes the direction of the pin motor
mot_dir = Pin(25, Pin.OUT)
mot_dir.on()

# Motor movement - pulse with timing between pulses controlling speed
mot_stp = Pin(26, Pin.OUT)
while True:
        
    mot_stp.on()
    sleep_us(1000)

    mot_stp.off()
    sleep_us(1000)
  
    

