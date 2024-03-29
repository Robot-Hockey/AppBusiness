#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)                            #define the pin that goes to the circuit
pin_to_circuit = 26

def rc_time (pin_to_circuit):
    count = 0                                       #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.01)                                 #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)             #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    if(count > 50):
     print('goal')
     time.sleep(2)     
    return count                                   #Catch when script is interupted, cleanup correctly

try:
    while True:
        print ( rc_time(pin_to_circuit))

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
