#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO

##############################
# Declarations and Inits
##############################

# Constants
GPIO_PIN_NUMBER = [5,10,1,2,4,7,11]

# GPIO Inits
GPIO.setmode(GPIO.BOARD)

for x in GPIO_PIN_NUMBER:
    GPIO.setup(x, GPIO.OUT)

userInput = ''

##############################
# Functions
##############################

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def gpio_clear():
    for i in GPIO_PIN_NUMBER:
        GPIO.output(i, False)

def gpio_turn_on(num):
    GPIO.output(num, True);

def gpio_read_letters(letters):
    for x in letters:
        if x == 'a':
            gpio_turn_on(12);
        elif x == 'b':
            gpio_turn_on(10);
        elif x == 'c':
            gpio_turn_on(8);
        elif x == 'd':
            gpio_turn_on(11);
        elif x == 'e':
            gpio_turn_on(7);
        elif x == 'f':
            gpio_turn_on(3);
        elif x == 'g':
            gpio_turn_on(5);

def gpio_show_number(num):
    if num == 0:
        gpio_read_letters("abcdef")
    if num == 1:
        gpio_read_letters("bc")
    if num == 2:
        gpio_read_letters("abged")
    if num == 3:
        gpio_read_letters("abgcd")
    if num == 4:
        gpio_read_letters("fgbc")
    if num == 5:
        gpio_read_letters("afgcd")
    if num == 6:
        gpio_read_letters("afgecd")
    if num == 7:
        gpio_read_letters("abc")
    if num == 8:
        gpio_read_letters("abcdefg")
    if num == 9:
        gpio_read_letters("abcfg")

def user_quit():
    gpio_clear()
    GPIO.cleanup()
    print("Buh-bye")

def user_clear():
    gpio_clear()

def user_help():
    print("h         - Help | What you are currently seeing")
    print("q         - Quit | Quit the application")
    print("<number>  - Displays <number> | Changes what number the LED shows to <number>")
    print("c         - Clear | Clears all LEDs")
    print("cd        - CountDown | Begins a countdown from 9 to 0 with 0.5s delays")
    print("p         - PartyTime! | Popped a Molly I\'m sweat\'n; Wooo!")

def user_party(s):
    gpio_read_letters("a")
    sleep(s)
    user_clear()
    gpio_read_letters("b")
    sleep(s)
    user_clear()
    gpio_read_letters("g")
    sleep(s)
    user_clear()
    gpio_read_letters("e")
    sleep(s)
    user_clear()
    gpio_read_letters("d")
    sleep(s)
    user_clear()
    gpio_read_letters("c")
    sleep(s)
    user_clear()
    gpio_read_letters("g")
    sleep(s)
    user_clear()
    gpio_read_letters("f")
    sleep(s)
    user_clear()

def main():
    print("Enter a command (type \'h\' for help):")
    while 1:
        userInput = raw_input("> ");
        gpio_clear()
        if (userInput == "q"):
            user_quit()
            break
        elif (userInput == "c"):
            user_clear()
        elif (userInput == "h"):
            user_help()
        elif (len(userInput) == 1 and is_number(userInput)):
            number = int(userInput)
            gpio_show_number(number)
        elif (userInput == "cd"):
            print("COUNTDOWN!")
            for x in range(0,10):
                x = 9 - x
                gpio_show_number(x)
                sleep(0.5)
                gpio_clear();
        elif (userInput == "p"):
            sleeptimer = 0.01;
            print("PARTY TIME!")
            for x in range(1, 11):
                x = 11 - x
                user_party(x*sleeptimer)
            for x in range(1, 11):
                user_party(x*sleeptimer)
        else:
            print("Invalid command, type \'h\' for help")

####################
# Main - start here
####################

main()
