# POO

# Abstraccion del mundo real a codigo, para generar un model

# Clase - Molde
class Auto:
    # Atributos - caracteristicas
    _gas = '95'  # privado

    def __init__(self, marca, color):  # contructor # __ metodos magicos
        self.marca = marca
        self.color = color

    # Metodos Acceso
    # get # set
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    # Metodos o Acciones
    def arrancar(self):
        print(f'Arranco el {self.marca}')

    def detenerse(self):
        print('Se detuvo')


# Objeto
auto1 = Auto('Kia', 'Rojo')
# auto1.color = 'Rojo'
# auto1.marca = 'Kia'
auto1.arrancar()
auto1.marca = 'Kia Picanto'
print(auto1.marca)  #

auto2 = Auto(color='Azul', marca='Toyota')
# auto2.color = 'Azul'
# auto2.marca = 'Toyota'
# auto2.arrancar()


