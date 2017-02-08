import RPi.GPIO as GPIO
from time import sleep

class Motor:
    def __init__(self, pwm, pina, pinb):
        # Definir modo de pines GPIO
        GPIO.setmode(GPIO.BCM)
        #Direccionar pines
        GPIO.setup(pina, GPIO.OUT)
        GPIO.setup(pinb, GPIO.OUT)
        GPIO.setup(pwm, GPIO.OUT)
        #Inicializar pwm en pin y definir frecuencia
        self.motor = GPIO.PWM(pwm,50)
        self.pina = pina
        self.pinb = pinb
        
    def avanza(self, pwm):
        GPIO.output(self.pinb, 1)
        GPIO.output(self.pina, 0)
        #Velocidad con que gira el motor
        self.motor.start(pwm)

    def retrocede(self, pwm):
        GPIO.output(self.pina, 1)
        GPIO.output(self.pinb, 0)
        #Velocidad con que gira el motor
        self.motor.start(pwm)    

    def alto(self):
        #Parar motor
        self.motor.stop()



