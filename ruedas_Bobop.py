from movimiento.Motor.Motor import *
from ojos.Ojos.Ojos import *
from time import sleep

motora = Motor(16, 20, 21)
motorb = Motor(13, 19, 26)
ojos = Ojos()

for x in range(10, 100, 10):
    motora.avanza(x)
    motorb.avanza(x)
    sleep(0.5)
    motora.retrocede(x)
    motorb.retrocede(x)
    sleep(0.5)

motora.alto()
motorb.alto()
sleep(0.5)

GPIO.cleanup()

