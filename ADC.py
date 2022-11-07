import machine
import time


print("Script begun ")
#setting pin 17 to power ADC
adc_pwr = machine.Pin(17, machine.Pin.OUT)
#setting pin 18 and 19 to SCl and SDA for ADC
i2c = machine.I2C(1, scl = machine.Pin(18), sda = machine.Pin(19), freq = 400000)

#turning on Power for ADC
adc_pwr.on()

print("scanning adc")
#Scanning I2C addresses and setting to 106 for load Cell and 108 for strain guage
address = i2c.scan() 

""" loop reading the ADC addresses and respective channels for structure see
https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
"""
count = 0

print("ADC powered on")
print("Count begin")

while True:
    
    #lc_data = i2c.readfrom_mem(address[0], 0, 2)
    print("Inside while loop")
    sg= i2c.readfrom(address[1], 2)
    m = b'\x0f\ff'
    result_int = int.from_bytes(sg, "big") & int.from_bytes(m, "big")
    ans = result_int.to_bytes(2, "big")
    print("count {} - Ohm change: {}". format(count, result_int))

 
    #print("Reading {}, load Cell info {}".format(count, lc_data))
    #print("Reading {}, strain guage info {}".format(count, sg))
    #int_val_sg = int.from_bytes(sg_data, "big")
    #print(int_val_sg)
    #print("load Cell info {} \nStrain Guage info {}".format(lc_data, sg_data))
    time.sleep(0.1)
    count = count + 1
    
    