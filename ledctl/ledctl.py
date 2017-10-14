from flask import Flask, request, jsonify
import pigpio
app = Flask(__name__)

#rgb 22, 27, 17
#base teal 40 97 15

GPIO_RED = 22
GPIO_GREEN = 27
GPIO_BLUE = 17
pi = pigpio.pi()

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

@app.route("/")
def home():
    return "Hello World!"

@app.route("/color")
def set_color():
    args = request.args.to_dict()
    r = to_PWM_dutycycle(args['r'])
    g = to_PWM_dutycycle(args['g'])
    b = to_PWM_dutycycle(args['b'])
    pi.set_PWM_dutycycle(GPIO_RED, r)
    pi.set_PWM_dutycycle(GPIO_GREEN, g)
    pi.set_PWM_dutycycle(GPIO_BLUE, b)
    return str(r) + ' ' + str(g) + ' ' + str(b)

@app.route("/get_color")
def get_color():
    r = pi.get_PWM_dutycycle(GPIO_RED)
    g = pi.get_PWM_dutycycle(GPIO_GREEN)
    b = pi.get_PWM_dutycycle(GPIO_BLUE)
    return jsonify({'red':r, 'green':g, 'blue':b})

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)

