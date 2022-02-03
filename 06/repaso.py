# Clases
# Tipado dinamico

class Jugador:
    # constructor
    def __init__(self, nombre):  # Constructor publicos
        self.nombre = nombre  # alcance global de clase
        self.__posicion = None  # privados

    def cambio_posicion(self, nueva_posicion):
        self.__posicion = nueva_posicion

    def ficha_tecnica(self):  # padre (nombre - posicion)
        print('Ficha tecnica del padre <Jugador>')
        print(f'> Nombre: {self.nombre}')
        print(f'> Posicion: {self.__posicion}')

    def get_posicion(self): # traer
        return self.__posicion

    def set_posicion(self, posicion): # enviar
        self.__posicion = posicion


class Albitro(Jugador):
    # parametro nacionalidad
    def __init__(self, nombre, nacionalidad):
        self.nacionalidad = nacionalidad
        Jugador.__init__(self, nombre)
        self.cambio_posicion('ALBITRO')

    def ficha_tecnica(self): # Hija  (nombre - posicion - nacionalidad)
        print('Ficha tecnica de Hijo <Albitro>')
        print(f'> Nombre: {self.nombre}')
        print(f'> Posicion: {self.get_posicion()} ')
        print(f'> Nacionalidad: {self.nacionalidad}')

arbitro01 = Albitro('Stip', 'Cubana')
arbitro01.ficha_tecnica()


class Arquero(Jugador):

    def __init__(self, nombre, edad):
        self.edad = edad
        Jugador.__init__(self, nombre)
        self.cambio_posicion('Arquero')

    # def ficha_tecnica(self): # Hijo (nombre edad posicion)
    #     print(f'Nombre {self.nombre}')
    #     print(f'Edad {self.edad}')
    #     print(f'Posicion {self._Jugador__posicion}')


# Crear una clase alquero que herede de Jugador y que imprima su nombre posicion y edad

#
# jugador1 = Jugador('Neymar')
# jugador1.cambio_posicion('delantero')
# jugador1.ficha_tecnica()  ## Nombre - Posicion # accion base
#
# albitro = Albitro('Estupiñan', 'Argentino')
# albitro.ficha_tecnica()  ## Nombre - posicion y nacionalidad # realicen otras acciones
#
# arquero1 = Arquero('Richart', 22)
# arquero1.ficha_tecnica()  ## Nombre - poscion - edad  # realicen otras acciones

# class Animal:
#     pass
#
# class Perro(Animal): #Herencia
#     pass
#
# #Herencia
# print(Perro.__bases__) # Muestrame tus padres
#
# # Sus hijos
# print(Animal.__subclasses__()) # Muestrame tus hijos
