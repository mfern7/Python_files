
class Circle_dos:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * Circle.pi
        print('el nuevo valor es:',self.radius)

    def getCircumference(self):
        return self.radius * Circle.pi * 2

    def size(self):
        if self.area > 5:
            return 'Grande'
            size1 = 'grande'
        else:
            return 'Chico'
            size1 = 'chico'

class Cricle_tres(Circle_dos):
    def __init__(self):
        print('Iniciando circulo')

    def categoria(self):
        if size1 == 'grande':
            return 'Muy grandeee'
        elif size1 == 'chico':
            return 'demasiado chico'

