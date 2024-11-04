from machine import Pin, I2C
import time

temp_addr = 24

def get_temp(i2c):
    i2c.writeto(temp_addr,bytearray([5]),False)
    rt=i2c.readfrom(temp_addr,2)
    t=(rt[0]&0x0f)*16+rt[1]/16.0
    if (rt[0]&0x10==0x10): #Negative
        t=t-256
    return t

#break
bpin=Pin(3,Pin.IN,Pin.Pull_UP)

#LED
led1=Pin(21,Pin.OUT)
led2=Pin(20,Pin.OUT)
led3=Pin(6,Pin.OUT)
led1.on()
led2.on()
led3.on()

#temp and accel - I2C0
i2c0=I2C(0,scl=Pin(5),sda=Pin(4),freq=4000000)
s=i2c0.scan()

while True:
    t=get_temp(i2c0)
    print(t)
    time.sleep(0.5)
    if bpin.value()==0:
        break