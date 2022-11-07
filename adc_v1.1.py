from machine import Pin, I2C
import time



#setting pin 17 to power ADC
adc_pwr = Pin(17, Pin.OUT)
#setting pin 18 and 19 to SCl and SDA for ADC
i2c = I2C(1, scl = Pin(18), sda = Pin(19), freq = 400000)

#turning on Power for ADC
adc_pwr.on()

#Scanning I2C addresses and setting to 106 for load Cell and 108 for strain guage
address = i2c.scan() 

""" loop reading the ADC addresses and respective channels for structure see
https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
"""

mod = b'\x93' #channel-1, g-8, 12-bit, continious.

m = b'\x0f\xff'

i2c.writeto(address[1], mod)
time.sleep(0.1)
    
    #lc_data = i2c.readfrom_mem(address[0], 0, 2)
while True:
    #reads D voltage from BRG 1
    sg= i2c.readfrom(address[1], 2)
    result_int = int.from_bytes(sg, "big") & int.from_bytes(m, "big")
    ans = result_int.to_bytes(2, "big")
    print("Reading: {}".format(sg))
    sg_int = int.from_bytes(ans, "big")
    print(sg_int)
    time.sleep(0.1)


 
 
    #print("Reading {}, load Cell info {}".format(count, lc_data))
    #print("Reading {}, strain guage info {}".format(count, sg))
    #int_val_sg = int.from_bytes(sg_data, "big")
    #print(int_val_sg)
    #print("load Cell info {} \nStrain Guage info {}".format(lc_data, sg_data))

    
    


