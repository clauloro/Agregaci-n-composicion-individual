class Cristal:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def get_area(self):
        return self.ancho * self.alto

class Ventana:
    def __init__(self, ancho, alto):
        self.cristal = Cristal(ancho, alto)

    def get_area(self):
        return self.cristal.get_area()

class ParedCortina:
    def __init__(self, ancho, alto):
        self.cristal = Cristal(ancho, alto)

    def get_area(self):
        return self.cristal.get_area()
    
ventana = Ventana(2, 1)
pared_cortina = ParedCortina(3, 2)

print("Área de la ventana: ", ventana.get_area())  
print("Área de la pared cortina: ", pared_cortina.get_area())