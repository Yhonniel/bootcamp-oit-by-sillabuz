print("Hola mundo!")

numero = 10  # int
cadena = 'Hola soy una cadena'  # str - string
boleano = True  # False # bool

print(type(numero))
print(type(cadena))
print(type(boleano))

octal = 0o10
decimal = 0x100

print(type(octal))
print(type(decimal))

real = 0.25
print(type(real))  # float

var_uno = 10
var_dos = 3

print(var_uno + var_dos)  # SUMA
print(var_uno - var_dos)  # RESTA O ADICION
print(var_uno * var_dos)  # MULTIPLICACION
print(var_uno / var_dos)  # DIVICION
print(var_uno % var_dos)  # MODULO
print(var_uno ** var_dos)  # POTENCIA
print(var_uno // var_dos)  # DIVICION ENTERA

# Operadores de asignacion
perro = 'Peluchin'

CONSTANTE = 100  # variable en mayuscula
# e indicar su valor al momento de declarar

a = 10
print("Valor inicial de a = " + str(a))
a += 5  # a = a + 5
print("Valor despues de un operador = " + str(a))
a -= 2  # a = a - a
print("Valor despues de un operador = " + str(a))

# cadenas
candena_comilla_soble = "COMILLAS DOBLES"
candena_comilla_simple = 'COMILLAS SIMPLES'

text = "cadena \n cadena"
print(text)
unicode = u"´dsfs´sfs"
raw = r"cadena \n cadena"
print(raw)

# Formateo de textos
nombre = "Yahyr"
apellido = "Paredes"
print(f"Hola me llamo {nombre} {apellido} ")  #
print("Hola me llamo {} {} ".format(nombre, apellido))  #

# Escribir una oracion con tres palabras
palabra_uno = 'rojo'
palabra_dos = 'mar'
palabra_tres = 'paseo'
oracion = f'Me fui de {palabra_tres} al {palabra_dos} y vi el ocaso de color {palabra_uno}'
print(oracion)

# Escapes
uno = "Hola \n mundo"  # Salto de linea
dos = "Hola \t mundo"  # Tabulacion

print(uno)
print(dos)

# Snack_case  # Python
nombre_apellidos = "asdasda asdasd"

# Separadores
print("Hola", "Mundo", sep="<-->")
print("Hola", end="Mundo ")
print("Hola", )

# Boleanos  bool
# True or False

# and or not => y | o | ¬

print(True and True)  # True
print(True or False)  # True
print(not False)  # True

# Operadores Relacionales

print(3 > 2)  # True o False
print(3 >= 2)  # True o False
print(3 <= 2)  # True o False
print(3 < 2)  # True o False
print(5 == 5)  # True o False
print(True == True)

input()

print("Ingrese su nombre:")
nombre = input()
print(f'Hola tu nombre es {nombre}')

edad = input("¿Cual es tu edad?")
print(edad)

# Condicionales
# IF
# ELSE
# ELIF = (ELSE IF)

# IF  ELIF ELSE
color = input("Ingrese un color: ")
if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
elif color == "verde":
    print("El color es verde")
elif color == "negro":
    print("El color es negro")
else:
    print("No encontramos tu color")

# Operador ternario
# JS IF RESUMINO
# condicion ? si: no

mayor_edad = 18
edad = int(input("Ingrese su edad: "))
# input tipo str

#  int > str
if edad >= mayor_edad:
    print(f"Eres mayor de edad y tienes {edad}")
else:
    print("Eres menor de edad")

edad = 17
# (false, true) [condicional]
validacion = ("Menor de edad", "Mayor de edad")[edad >= 18]
print(validacion)
# True   if condicional else (false)
respuesta = "mayor de edad" if edad >= 18 else "Menor de edad"  # Esta se usa mas
print(respuesta)

# BLUCLE
# WHILE AND FOR

# Bucle infinito
edad = 0  # 18
while edad < 18:  # 18 < 18 False (Detiene)
    edad += 1  # edad  + 1
    print(f"Tu edad es {edad}")

# TIPOS BASICOS
# numeros ( int - float)
# cadenas (str)
# booleanos (bool)

print(10 % 3)  # Modulo
print(10 ** 3)  # Potencia
print(10 // 3)  # Divicion entera

cadena = " Hoy gano peru!"
print(f'{cadena} a los ultimos minutos')

nombre = input("Ingrese su nombre: ")
print(f"Tu nombre es : {nombre}")

# if (condicional):
#     ....
# elif ():
#     ..
#     else:
#     ..


# Hoy es el cumpleaños de Yhoniel
# Crear una lista de invitados donde solo se guardara
# el nombre del invitado que traiga regalo
# al final imprimir la lista de invitados

invitados = ''
condicion = True
while condicion:  # CONDICIONAL
    invitado = input("¿Cual es tu nombre?")
    regalo = input("Trae regalo <S/N>")
    if regalo == 'S' or regalo == 's':
        invitados += f"{invitado}, "

    continuar = input("Deseas agregar otro invitado <S/N>")
    if continuar == 'N':  # BUSQUEDA DATOS
        condicion = False
        # break

print(invitados)

# colecciones
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
