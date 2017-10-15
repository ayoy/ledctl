from time import sleep           # Allows us to call the sleep function to slow down our loop
import helpers
import pigpio
from colorsys import rgb_to_hls, hls_to_rgb
 
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
    (h, l, s) = rgb_to_hls(float(red)/255, float(green)/255, float(blue)/255)
    print((h, l, s))
    cl = 0
    while True:
        (r, g, b) = hls_to_rgb(h, cl, s)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pi.set_PWM_dutycycle(22, r)
        pi.set_PWM_dutycycle(27, g)
        pi.set_PWM_dutycycle(17, b)
        print((r, g, b))
        cl = cl + 0.005
        if cl > l:
            cl = l
        sleep(0.05)
        if cl >= l:
            break


def fade_out(red, green, blue):
    (h, l, s) = rgb_to_hls(float(red)/255, float(green)/255, float(blue)/255)
    print((h, l, s))
    cl = l
    while True:
        (r, g, b) = hls_to_rgb(h, cl, s)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pi.set_PWM_dutycycle(22, r)
        pi.set_PWM_dutycycle(27, g)
        pi.set_PWM_dutycycle(17, b)
        print((r, g, b))
        cl = cl - 0.005
        if cl < 0:
            cl = 0
        sleep(0.05)
        if cl <= 0:
            pi.set_PWM_dutycycle(22, 0)
            pi.set_PWM_dutycycle(27, 0)
            pi.set_PWM_dutycycle(17, 0)
            break


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

    sleep(0.1)           # Sleep for a full second before restarting our loop


