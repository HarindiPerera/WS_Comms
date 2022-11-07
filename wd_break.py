from machine import Pin
import time


# PIN 0 1 2 
#     0 1 0 30ms
#     0 0 1 100ms
#     1 0 1 1sec 
#     0 1 1 10sec
#     1 1 1 60sec



#Prototype board Pinout


wdo = Pin(2, Pin.IN)                    # Watch dog trigger indicator 
red = Pin(4, Pin.OUT)                   # RED output indicator 


# wd1 = Pin(4, OUT)                     # WD1 pulse toggle 


'''
if wdo.value == 1:
        print("High")
    elif wdo.value == 0:
        print("Low")
    else:
        print("error")

'''
'''
def pulse(void):
    wd1.value(0)
    time.sleep(0.5)
    wd1.value(1)
    time.sleep(0.5)
'''


#Watch dog pulses after timeout period
while True:
    print(wdo.value())