from flask import Flask, render_template
from movimiento.Motor.Motor import *
from ojos.Ojos.Ojos import *
from time import sleep

motora = Motor(16, 20, 21)
motorb = Motor(13, 19, 26)
ojos = Ojos()

app = Flask(__name__)

@app.route("/")

def hello():
   templateData = {
      'title' : 'HELLO!',
      }
   return render_template('main.html', **templateData)


@app.route("/<changePin>/<action>")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80, debug=True)
