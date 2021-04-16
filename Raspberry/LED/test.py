import RPi.GPIO as GPIO
import time


#pins = [25,21,20,16,12,26,19,13]
pins = [21,20,16,12,26,19]
allpins = [23,24,21,20,16,12,26,19]
#allpins = [23,24,25,21,20,16,12,26,19,13]

bit0 = 23
bit1 = 24
BITS = [bit0,bit1]

 

GPIO.setmode(GPIO.BCM)

for pin in allpins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)

GPIO.output(BITS,GPIO.LOW)

for i in range(10):
    GPIO.output(pins,0)
    time.sleep(1)
    GPIO.output(pins,1)
    time.sleep(1)

GPIO.cleanup()

