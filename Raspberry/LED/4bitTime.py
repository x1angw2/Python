import RPi.GPIO as GPIO
import time



'''
BIT0 = 21
BIT1 = 13
BIT2 = 19
BIT3 = 26
A  = 6
B  = 5
C  = 16
D  = 12
E  = 4
F  = 17
G  = 27
DP = 20

1 = [5,16]
2 = [6,5,12,4,27]
3 = [6,5,16,12,27]
4 = [5,16,17,27]
5 = [6,16,12,17,27]
6 = [6,16,12,4,17,27]
7 = [6,5,16]
8 = [6,5,16,12,4,17,27,20]
9 = [6,5,16,12,17,27]
0 = [6,5,16,12,4,17]
'''
pins = [27,17,4,12,16,5,6,20]
bitpins = [21,13,19,26]
BIT0 = [21]
BIT1 = [13]
BIT2 = [19]
BIT3 = [26]
allpins = [27,17,4,12,16,5,6,20,21,13,19,26]

one = [5,16]
two = [6,5,12,4,27]
three = [6,5,16,12,27]
four = [5,16,17,27]
five = [6,16,12,17,27]
six = [6,16,12,4,17,27]
seven = [6,5,16]
eight = [6,5,16,12,4,17,27]
nine = [6,5,16,12,17,27]
zero = [6,5,16,12,4,17]

one2zero = [zero,one,two,three,four,five,six,seven,eight,nine]

GPIO.setmode(GPIO.BCM)

# 读取当前时间
def nowTime():
    all_time = time.localtime()
    tm_hour = all_time.tm_hour
    tm_min = all_time.tm_min
    tm_sec = all_time.tm_sec
    return tm_hour,tm_min,tm_sec


def light(bit,pins,tm):
    all_pin = bit + pins
    down_bit = list(set(bitpins) - set(bit))
    GPIO.setup(all_pin,GPIO.OUT)
    GPIO.setup(down_bit,GPIO.OUT)
    GPIO.output(down_bit,GPIO.HIGH)
    GPIO.output(bit,GPIO.LOW)
    for i in range(1):
        GPIO.output(pins,GPIO.HIGH)
        time.sleep(tm)
        GPIO.output(pins,GPIO.LOW)
        time.sleep(tm)
    # GPIO.cleanup()

def BitNum(bit,bit_num):
    if bit_num == 0:
        light(bit=bit,pins=zero,tm=0.002)
    if bit_num == 1:
        light(bit=bit,pins=one,tm=0.002)
    if bit_num == 2:
        light(bit=bit,pins=two,tm=0.002)
    if bit_num == 3:
        light(bit=bit,pins=three,tm=0.002)
    if bit_num == 4:
        light(bit=bit,pins=four,tm=0.002)
    if bit_num == 5:
        light(bit=bit,pins=five,tm=0.002)
    if bit_num == 6:
        light(bit=bit,pins=six,tm=0.002)
    if bit_num == 7:
        light(bit=bit,pins=seven,tm=0.002)
    if bit_num == 8:
        light(bit=bit,pins=eight,tm=0.002)
    if bit_num == 9:
        light(bit=bit,pins=nine,tm=0.002)

def flashing():
    while True:
        now_time = nowTime()
        bit0_num = now_time[0] // 10
        bit1_num = now_time[0] % 10
        bit2_num = now_time[1] // 10
        bit3_num = now_time[1] % 10
        bit4_num = now_time[2] // 10
        bit5_num = now_time[2] % 10

        BitNum(BIT0,bit2_num)
        BitNum(BIT1,bit3_num)
        BitNum(BIT2,bit4_num)
        BitNum(BIT3,bit5_num)


if __name__ == '__main__':
    flashing()
    GPIO.cleanup()
