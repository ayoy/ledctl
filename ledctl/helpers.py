import pigpio

GPIO_RED = 22
GPIO_GREEN = 27
GPIO_BLUE = 17

# values as per https://stackoverflow.com/a/596243/969818
Y_RED = 0.299
Y_GREEN = 0.587
Y_BLUE = 0.114


class Color(dict):
    def __init__(self, *args, **kwargs):
        super(Color, self).__init__(**kwargs)
        if len(args) == 1:
            dictionary = args[0]
            self['red'] = to_PWM_dutycycle(dictionary['r'])
            self['green'] = to_PWM_dutycycle(dictionary['g'])
            self['blue'] = to_PWM_dutycycle(dictionary['b'])
        elif len(args) == 3:
            self['red'] = args[0]
            self['green'] = args[1]
            self['blue'] = args[2]

    @property
    def red(self):
        return self['red']

    @property
    def green(self):
        return self['green']

    @property
    def blue(self):
        return self['blue']

    @property
    def bred(self):
        return Y_RED * self.red

    @property
    def bgreen(self):
        return Y_GREEN * self.green

    @property
    def bblue(self):
        return Y_BLUE * self.blue



def to_PWM_dutycycle(string):
    try:
        i = int(string)
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        return i
    except ValueError:
        return 0


def get_current_color(pi):
    r = pi.get_PWM_dutycycle(GPIO_RED)
    g = pi.get_PWM_dutycycle(GPIO_GREEN)
    b = pi.get_PWM_dutycycle(GPIO_BLUE)
    return Color(r, g, b)
