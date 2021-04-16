import RPi.GPIO as GPIO
import time

'''
2位七段数码管
3621AS-1
共阴

针脚位
25 = DP
21 = A
20 = B
16 = C
12 = D
26 = E
19 = F
13 = G
23 = DIG1
24 = DIG2
'''



pin_0 = [12,26,19,21]
pin_1 = [21,20,16,12]
pins = [21,20,16,12,26,19,13,25]
allpins = [23,24,21,20,16,12,26,19,13,25]
bit0 = 23
bit1 = 24
BITS = [bit0,bit1]

# 设置模式
GPIO.setmode(GPIO.BCM)

# 所有节点打开,并且设置为HIGH
for pin in allpins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)

def one():
    GPIO.output(BITS,GPIO.LOW)

    for i in range(3):
        GPIO.output(pins,GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(pins,GPIO.LOW)
        time.sleep(0.4)

def two():
    def circle(bit_start,bit_end,pin,n):
        GPIO.output(bit_end,GPIO.HIGH)
        GPIO.output(bit_start,GPIO.LOW)

        for i in pin:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(n)
            GPIO.output(i,GPIO.LOW)
    k = 0.07
    a = 1
    while a < 6:
        circle(bit1,bit0,pin_1,k)
        circle(bit0,bit1,pin_0,k)
        a += 1

def three():
    GPIO.output(allpins,GPIO.LOW)
    num_1 = [20,16]
    num_2 = [21,20,12,26,13]
    num_3 = [21,20,16,12,13]
    num_4 = [20,16,19,13]
    num_5 = [21,16,12,19,13]
    num_6 = [21,16,12,26,19,13]
    num_7 = [21,20,16]
    num_8 = [21,20,16,12,26,19,13]
    num_9 = [21,20,16,12,19,13]


    nums = [num_9,num_8,num_7,num_6,num_5,num_4,num_3,num_2,num_1]

    for num in nums:
        GPIO.output(num,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(num,GPIO.LOW)


def four():
    H = [20,16,26,19,13]
    I = [20,16]
    n = 1
    while n < 999:
        GPIO.output(bit0,GPIO.LOW)
        GPIO.output(H,GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(bit0,GPIO.HIGH)
        GPIO.output(H,GPIO.LOW)

        GPIO.output(bit1,GPIO.LOW)
        GPIO.output(I,GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(bit1,GPIO.HIGH)
        GPIO.output(I,GPIO.LOW)
        
        n += 1

# 全部灯闪烁
one()
# 转圈
two()
# 倒数
three()
# 显示字符 H I
four()


GPIO.cleanup()


