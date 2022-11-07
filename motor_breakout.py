from machine import Pin
from time import sleep_us


print("Operational tests are ready to run!")

step = 0

# Changes the direction of the pin motor
#change pin for mot dir 
mot_dir = Pin(25, Pin.OUT)
mot_dir.on()


# Motor movement - pulse with timing between pulses controlling speed
#change pin for mot step
mot_stp = Pin(33, Pin.OUT)

for x in range(24072):
    mot_stp.on()
    sleep_us(500)
    mot_stp.off()
    sleep_us(500)
    print("Steps", x)
    