import RPi.GPIO as GPIO
import time

N = 4
P = 17
pins = [N,P]

GPIO.setmode(GPIO.BCM)

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    
for i in range(30):
    GPIO.output(N,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(N,GPIO.LOW)
    time.sleep(0.1)

GPIO.cleanup()
