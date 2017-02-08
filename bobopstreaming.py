from flask import Flask, render_template, request, redirect, url_for, make_response, Response
from movimiento.Motor.Motor import *
from ojos.Ojos.Ojos import *
from time import sleep
from camera import Camera

motora = Motor(16, 20, 21)
motorb = Motor(13, 19, 26)
ojos = Ojos()

app = Flask(__name__)

@app.route("/")

def index():
   return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
              b'Content-Type: image&jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
   return Response(gen(Camera()),
                   mimetype = 'multipart/x-mixed-replace; boundary=frame')


@app.route('/<boton>', methods=['POST'])
def reroute(boton):
    boTon = int(boton)
    if boTon == 1:
        motora.avanza(70)
    elif boTon == 2:
        motorb.avanza(70)
    elif boTon == 3:
        motora.retrocede(70)
    elif boTon == 4:
        motorb.retrocede(70)
    else:
        motora.alto()
        motorb.alto()

    response = make_response(redirect(url_for('index')))
    return(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80, debug=True)

GPIO.cleanup()
