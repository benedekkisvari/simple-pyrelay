from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        for pin in pins:
            state = int(request.form.get(str(pin), 0))
            GPIO.output(pin, state)

    # Get the current status of the pins
    current_status = {pin: GPIO.input(pin) for pin in pins}
    
    return render_template('index.html', pins=pins, current_status=current_status)

@app.route('/shutdown')
def shutdown():
    GPIO.cleanup()
    return "GPIO cleaned up and server shutting down."

if __name__ == '__main__':
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)
    pins = [18, 17, 15, 14]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    try:
        app.run(host='0.0.0.0', port=80)
    except KeyboardInterrupt:
        GPIO.cleanup()

