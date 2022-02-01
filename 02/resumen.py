# COLECCIONES
# LISTAS

# OPERACIONEs  # ADD REMOVE
#        1 ,  2 ,  3  ,  4   ,     5    ,   6
lista = [1, 0.85, True, False, [1, 2, 3], "Texto"]

for item in lista:
    print(item)

print(lista)
print(len(lista))
# Type
print(type(lista))  # <list>
# SLICING
print(lista[2])
print(lista[-1])
print(lista[:-2])  # - solicitar el elemnto de derecha a izquierda segun indice
print(lista[:2])
print(lista[100])

numeros = [1, 2, 3, 4, 5]  # sin importar el indice
print(numeros)
numeros.append(7)  # Agrega en el ultimo indice
numeros.append(8)  # Agrega en el ultimo indice
numeros.append(9)  # Agrega en el ultimo indice
print(numeros)

# indice, valor
numeros.insert(3, 10)
print(numeros)

numeros = [1, 2, 3, 4, 5]  #
num = numeros.pop()
print(num)  # imprimiendo el valor que estoy eliminando
print(numeros)

# remove

animales = ["gato", "perro", "caballo"]
print(animales)
animales.remove("perro")
print(animales)

del animales[0]
print(animales)

del animales[:]
print(animales)

# CONST
GATO = "miau"  #

# TUPLAS peso a nivel de memoria () INMUTABLE

tupla = ('python', 'java', 'c', 'c++')
print(type(tupla))  # tuple

# slicing
print(tupla[0])

# ROLES
roles = ('admin', 'user', 'guest')

# DICCIONARIOS
diccionarios = {'key': 'value'}
print(type(diccionarios))  # dict

lenguaje = {"python": 1991, "c": 1972, "java": 1996}  # pithon
print(lenguaje)
# lenguaje[1]
print(lenguaje['python'])

# Asignacion
lenguaje['python'] = 2001
print(lenguaje['python'])

# add
lenguaje['c++'] = 1983
print(lenguaje)

# eliminar
lenguaje.pop('python')
print(lenguaje)

# None == NULL
print(lenguaje['pithon'])  # exeptcion
print(lenguaje.get('pithon'))  # None

print(lenguaje.get('django') is None)

lenguaje = {
    # key  : value
    'python': 1991,
    "c": 1972,
    "java": 1996
}

print(lenguaje['python'])
print(lenguaje['c'])
print(lenguaje['java'])

for key in lenguaje:
    print(f"llave: {key} => valor: {lenguaje[key]}")

for k, v in lenguaje.items():
    print(f"llave : {k}")
    print(f"value : {v} \n")
