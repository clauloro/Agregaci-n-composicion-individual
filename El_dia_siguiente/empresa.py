class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.empleados = []
        
    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ubicacion = None

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        
    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

class Edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        ciudad.agregar_edificio(self)

new_york = Ciudad("New York")
los_angeles = Ciudad("Los Ángeles")

edificio_a = Edificio("A", new_york)
edificio_b = Edificio("B", new_york)
edificio_c = Edificio("C", los_angeles)

yoohoo = Empresa("YooHoo!")

yoohoo.agregar_edificio(edificio_a)
yoohoo.agregar_edificio(edificio_b)
yoohoo.agregar_edificio(edificio_c)

martin = Empleado("Martin")
salim = Empleado("Salim")
xing = Empleado("Xing")

yoohoo.agregar_empleado(martin)
yoohoo.agregar_empleado(salim)
yoohoo.agregar_empleado(xing)

def destruir_ciudad(ciudad):
    ciudad.edificios = []

destruir_ciudad(new_york)

for empleado in yoohoo.empleados:
    if empleado.ubicacion in new_york.edificios:
        empleado.ubicacion = None
