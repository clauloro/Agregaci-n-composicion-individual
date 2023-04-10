class Cristal:
    def __init__(self, transparencia):
        self.transparencia = transparencia

    def cambiar_transparencia(self, nueva_transparencia):
        self.transparencia = nueva_transparencia
        print(f"La transparencia del cristal ahora es {self.transparencia}.")


class Ventana:
    def __init__(self, transparencia):
        self.cristal = Cristal(transparencia)

    def cambiar_transparencia(self, nueva_transparencia):
        self.cristal.cambiar_transparencia(nueva_transparencia)


class ParedCortina:
    def __init__(self, transparencia, ventanas=[]):
        self.cristal = Cristal(transparencia)
        self.ventanas = ventanas

    def cambiar_transparencia(self, nueva_transparencia):
        self.cristal.cambiar_transparencia(nueva_transparencia)
        for ventana in self.ventanas:
            ventana.cambiar_transparencia(nueva_transparencia)

ventana1 = Ventana(50)
ventana2 = Ventana(70)

pared_cortina = ParedCortina(80, [ventana1, ventana2])

ventana1.cambiar_transparencia(40)
ventana2.cambiar_transparencia(60)
pared_cortina.cambiar_transparencia(90)
