class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, empresa):
        super().__init__(nombre)
        self.empresa = empresa

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)
        edificio.ciudad = self

    def destruir(self):
        for edificio in self.edificios:
            for empleado in edificio.empleados:
                del empleado
            del edificio
        del self

class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.ciudad = None

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.empresa.agregar_edificio(self)

yoo_hoo = Empresa('YooHoo!')
martin = Empleado('Sr. Martin', yoo_hoo)
salim = Empleado('Salim', yoo_hoo)
xing = Empleado('Sra. Xing', yoo_hoo)
edificio_a = Edificio('A')
edificio_b = Edificio('B')
edificio_c = Edificio('C')
new_york = Ciudad('New York')
los_angeles = Ciudad('Los Angeles')

yoo_hoo.agregar_ed