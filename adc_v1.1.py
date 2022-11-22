from machine import Pin, I2C
import time

""" loop reading the ADC addresses and respective channels for structure see
https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
"""

#defing
COUNT = 5

#setting pins to power ADC
adc_l_pwr = Pin(16, Pin.OUT)
adc_r_pwr = Pin(17, Pin.OUT)

#setting SCl and SDA for ADC
i2c = I2C(1, scl = Pin(22), sda = Pin(21), freq = 400000)

#turning on left hand Power for ADC
adc_l_pwr.on()

#turning on right hand side Power for ADC
adc_r_pwr.on()


#Scanning I2C addresses and setting to 106 for load Cell and 108 for strain guage
address = i2c.scan() 


print("i2c adresses :" , address)

mod = b'\x93' #channel-1, g-8, 12-bit, continious.

m = b'\x0f\xff'

i2c.writeto(address[1], mod)
time.sleep(0.1)
    

for x in range(COUNT):
    
    #reads D voltage from BRG 1
    sg= i2c.readfrom(address[1], 2)
    result_int = int.from_bytes(sg, "big") & int.from_bytes(m, "big")
    ans = result_int.to_bytes(2, "big")    
    sg_data = int.from_bytes(ans, "big")
      
    time.sleep(0.1)
    
    lc_data = i2c.readfrom_mem(address[0], 0, 2)
    print("Reading {}, load Cell Info {}".format(x+1, lc_data))
    print("Reading {}, strain guage Info {}".format(x+1, sg))
    
    #int_val_sg = int.from_bytes(sg_data, "big")
    #print(int_val_sg)
    print("load Cell info {} \nStrain gauge info {}\n".format(lc_data, sg_data)
