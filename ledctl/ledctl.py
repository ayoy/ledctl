from flask import Flask, request, jsonify
from helpers import *
import pigpio
app = Flask(__name__)

#rgb 22, 27, 17
#base teal 40 97 15

pi = pigpio.pi()

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
    color = get_current_color(pi)
    return jsonify(color)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)

