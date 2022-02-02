# HERENCIA

# Padre # Vehiculo
# Hijo  # Taxi

# class Vehiculo:
#
#     def __init__(self, placa, marca):
#         self.placa = placa
#         self.marca = marca
#
#     def getPlaca(self):  # traer
#         return self.placa
#
#     def getMarca(self):  # traer
#         return self.marca
#
#
# # Hijo hereda del (padre)
# class Taxi(Vehiculo):
#     # Combinaciones en el constructor
#
#     # #TAXIS DE LA MISMA MARCA Y PLACA
#     # def __init__(self):
#     #     Vehiculo.__init__(self,'ABC123', 'Corolla') # ARGUMENTOS
#
#     # def __init__(self, placa, marca, tipo_permiso):
#     #     self.tipo_permiso = tipo_permiso
#     #     Vehiculo.__init__(self, placa=placa, marca=marca) # vehiculo aqui estan la placa y la marca
#
#     def hacer_colectivo(self):
#         print('hacer colecctivo')
#
#
# vehiculo1 = Vehiculo('BXM-123', 'Audi')
# print(f'La placa de mi vehiculo es {vehiculo1.getPlaca()}')
#
# # taxi1 = Taxi('ABC-123', '123')
# # taxi1 = Taxi('Colectivo')
# taxi1 = Taxi('ABC-123', 'Corolla', 'Colectivo')
# # taxi1 = Taxi()
# print(f'La placa de mi taxi es {taxi1.getPlaca()}')
# taxi1.hacer_colectivo()  #


class Persona:
    # -nombre
    # -dni
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def hablar(self, mensaje):
        print(f'Hola mi nombre es {self.nombre} y tengo una mensaje: {mensaje} ')


# class Supervisor(Persona):
class Supervisor(Persona):
    # APELLIDO
    def __init__(self, nombre, dni, apellido):
        # Persona.__init__(self, 'Juan', 12345678)# Manera statica
        Persona.__init__(self, nombre, dni)  # <--
        self.apellido = apellido

    def print_apellido(self):
        print(f'Hola mi apellido es {self.apellido}')

    def full_name(self):
        print(f'{self.nombre} {self.apellido}')


# supervisor_uno = Supervisor(nombre='Juan', dni=78542136)
# supervisor_uno.hablar('Soy un objeto de la clase supervisor que hereda de Persona')

supervisor_dos = Supervisor('Yahyr', 78456122, 'Paredes')
supervisor_dos.print_apellido()
supervisor_dos.hablar('SOY UN MENSAJE')
supervisor_dos.full_name()

supervisor_tres = Supervisor('Pedro', 12345678, 'Castillo')
supervisor_tres.print_apellido()
supervisor_tres.hablar('')
supervisor_tres.full_name()
