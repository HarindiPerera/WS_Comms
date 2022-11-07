from machine import Pin
import time


# PIN 0 1 2 
#     0 1 0 30ms
#     0 0 1 100ms
#     1 0 1 1sec 
#     0 1 1 10sec
#     1 1 1 60sec

red_led = Pin(0,Pin.OUT)                    # ESP32 enable pin indicator 
watchdog = Pin(2, Pin.IN)                   # Watch dog trigger indicator 
x = Pin(4,Pin.OUT)                          # Act as WD1 pulse


#Toggle green using wd1 pulse
def toggle (void):
    x.value(0)
    time.sleep(0.5)
    x.value(1)
    time.sleep(0.5)


#track wd timer cycles
def trigger (void):
    print("triggered")


#Watch dog pulses after timeout period
while True:
    
    if watchdog.value() == 1:
        red_led(0)
    
    elif watchdog.value() == 0:
        red_led(1)

