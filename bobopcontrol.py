from flask import Flask, render_template, request, redirect, url_for, make_response
from movimiento.Motor.Motor import *
from ojos.Ojos.Ojos import *
from time import sleep
import os

motora = Motor(16, 20, 21)
motorb = Motor(13, 19, 26)
ojos = Ojos()

app = Flask(__name__)

@app.route("/")

def indexsc():
   return render_template('indexsc.html')


@app.route('/<boton>', methods=['POST'])
def reroute(boton):
   boTon = int(boton)
   if boTon == 1:
      motora.avanza(100)
      motorb.avanza(100)
   elif boTon == 2:
      motora.retrocede(100)
      motorb.retrocede(100)
   elif boTon == 3:
      motora.avanza(100)
      motorb.retrocede(100)
   elif boTon == 4:
      motorb.avanza(100)
      motora.retrocede(100)
   elif boTon == 5:
      motora.alto()
      motorb.alto()


    
   elif boTon == 6:
      ojos.abiertos()
   elif boTon == 7:
      ojos.cerrados()
   elif boTon == 8:
      ojos.guino()
      sleep(0.5)
      ojos.abiertos()
   elif boTon == 9:
      ojos.feliz()
   elif boTon == 10:
      ojos.cerrados()
      sleep(0.5)
      ojos.abiertos()
   elif boTon == 11:
      ojos.dormido()
   elif boTon == 12:
      os.system("sudo shutdown -h now")
   else:
      pass

   response = make_response(redirect(url_for('indexsc')))
   return(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8765, debug=True)

GPIO.cleanup()
