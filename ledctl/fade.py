from time import sleep
from helpers import *
import pigpio
 
pi = pigpio.pi()

oldinput = 0
r = pi.get_PWM_dutycycle(22)
g = pi.get_PWM_dutycycle(27)
b = pi.get_PWM_dutycycle(17)
print((r, g, b))
pi.set_PWM_dutycycle(22, 0)
pi.set_PWM_dutycycle(27, 0)
pi.set_PWM_dutycycle(17, 0)

def fade_in(red, green, blue):
    color = Color(red, green, blue)
    bred = color.bred
    bgreen = color.bgreen
    bblue = color.bblue
    cb = 0
    step = 0.01
    while True:
        (r, g, b) = (int(cb * bred / Y_RED), int(cb * bgreen / Y_GREEN), int(cb * bblue / Y_BLUE))
        pi.set_PWM_dutycycle(22, r)
        pi.set_PWM_dutycycle(27, g)
        pi.set_PWM_dutycycle(17, b)
        #print((r, g, b))
        if cb > 1:
            break
        cb = cb + step
        sleep(0.025)


def fade_out(red, green, blue):
    color = Color(red, green, blue)
    bred = color.bred
    bgreen = color.bgreen
    bblue = color.bblue
    cb = 1
    step = 0.01
    while True:
        (r, g, b) = (int(cb * bred / Y_RED), int(cb * bgreen / Y_GREEN), int(cb * bblue / Y_BLUE))
        pi.set_PWM_dutycycle(22, r)
        pi.set_PWM_dutycycle(27, g)
        pi.set_PWM_dutycycle(17, b)
        #print((r, g, b))
        if cb < 0:
            break
        cb = cb - step
        sleep(0.025)


# Start a loop that never ends
while True:
    input = pi.read(21)
    if input == 1 and oldinput == 0:
        print('movement detected')
        print((r, g, b))
        fade_in(r, g, b)
        sleep(2)
    elif input == 0 and oldinput == 1:
        print('fading out')
        fade_out(r, g, b)
    
    oldinput = input

    sleep(0.1)


