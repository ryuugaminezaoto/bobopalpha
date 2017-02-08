import max7219.led as led
from time import sleep

class Ojos:
    
    def __init__(self):
        self.device = led.matrix(cascaded = 2)

    def dormido(self):
        for i in range(0, 16):
            for j in range(0, 8):
                self.device.pixel(i,j,0)

    def abiertos(self):
        self.dormido()
        for i in range(1, 15):
            for j in range(1, 7):
                if (i == 7) or (i == 8):
                    pass
                else:
                    self.device.pixel(i,j,1)

        self.device.pixel(2,0,1)
        self.device.pixel(2,7,1)
        self.device.pixel(3,0,1)
        self.device.pixel(3,7,1)
        self.device.pixel(4,0,1)
        self.device.pixel(4,7,1)
        self.device.pixel(5,0,1)
        self.device.pixel(5,7,1)
        self.device.pixel(10,0,1)
        self.device.pixel(10,7,1)
        self.device.pixel(11,0,1)
        self.device.pixel(11,7,1)
        self.device.pixel(12,0,1)
        self.device.pixel(12,7,1)
        self.device.pixel(13,0,1)
        self.device.pixel(13,7,1)

    def cerrados(self):
        self.dormido()
        for i in range(0, 16):
            for j in range(3, 5):
                self.device.pixel(i,j,1)

    def guino(self):
        self.dormido()
        for i in range(1, 7):
            for j in range(1, 7):
                self.device.pixel(i,j,1)

        self.device.pixel(2,0,1)
        self.device.pixel(2,7,1)
        self.device.pixel(3,0,1)
        self.device.pixel(3,7,1)
        self.device.pixel(4,0,1)
        self.device.pixel(4,7,1)
        self.device.pixel(5,0,1)
        self.device.pixel(5,7,1)
        self.device.pixel(10,0,1)
        self.device.pixel(11,0,1)
        self.device.pixel(12,0,1)
        self.device.pixel(13,0,1)
        self.device.pixel(9,2,1)
        self.device.pixel(9,3,1)
        self.device.pixel(9,4,1)
        self.device.pixel(10,1,1)
        self.device.pixel(10,2,1)
        self.device.pixel(10,3,1)
        self.device.pixel(11,1,1)
        self.device.pixel(11,2,1)
        self.device.pixel(12,1,1)
        self.device.pixel(12,2,1)
        self.device.pixel(13,1,1)
        self.device.pixel(13,2,1)
        self.device.pixel(13,3,1)
        self.device.pixel(14,2,1)
        self.device.pixel(14,3,1)
        self.device.pixel(14,4,1)

    def feliz(self):
        self.dormido()

        self.device.pixel(2,0,1)
        self.device.pixel(3,0,1)
        self.device.pixel(4,0,1)
        self.device.pixel(5,0,1)
        self.device.pixel(1,2,1)
        self.device.pixel(1,3,1)
        self.device.pixel(1,4,1)
        self.device.pixel(2,1,1)
        self.device.pixel(2,2,1)
        self.device.pixel(2,3,1)
        self.device.pixel(3,1,1)
        self.device.pixel(3,2,1)
        self.device.pixel(4,1,1)
        self.device.pixel(4,2,1)
        self.device.pixel(5,1,1)
        self.device.pixel(5,2,1)
        self.device.pixel(5,3,1)
        self.device.pixel(6,2,1)
        self.device.pixel(6,3,1)
        self.device.pixel(6,4,1)
        
        self.device.pixel(10,0,1)
        self.device.pixel(11,0,1)
        self.device.pixel(12,0,1)
        self.device.pixel(13,0,1)
        self.device.pixel(9,2,1)
        self.device.pixel(9,3,1)
        self.device.pixel(9,4,1)
        self.device.pixel(10,1,1)
        self.device.pixel(10,2,1)
        self.device.pixel(10,3,1)
        self.device.pixel(11,1,1)
        self.device.pixel(11,2,1)
        self.device.pixel(12,1,1)
        self.device.pixel(12,2,1)
        self.device.pixel(13,1,1)
        self.device.pixel(13,2,1)
        self.device.pixel(13,3,1)
        self.device.pixel(14,2,1)
        self.device.pixel(14,3,1)
        self.device.pixel(14,4,1)


    def mensaje(self, men):
        self.men = men
        self.device.show_message(men)
