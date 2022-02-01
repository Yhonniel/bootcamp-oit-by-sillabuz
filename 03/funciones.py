# def mi_funcion(nombre, apellido):
#     print(f"Hola mi nombre es {nombre} {apellido}")
#     # Bloque de codigo
#     # return None


# mi_funcion("Yahyr", "Paredes")
# # mi_funcion("Juan")
# # mi_funcion("Pedro")


# Crear una funcion que me pertisa sumar dos numeros
# pero si no envio el segundo numero se debe sumar
# por 10 al primero numero

# Parametros opcional
# def sumar(a, b=10):
#     sumar = a + b
#     print(sumar)
#
# sumar(1, 2)  # 3
# sumar(100)  # 110


# Escribir una función que muestre por pantalla el saludo
# ¡Hola Yahyr! cada vez que se la invoque.

# def saludo(nombre):
#     print(f"Hola {nombre}")
#
# saludo("Yahyr")


# Escribir una función que calcule el total de una factura tras aplicarle un descuento.
# La función debe recibir la cantidad sin descuento y el descuento a aplicar,
# y devolver el total de la factura. Si se invoca la función sin pasarle el descuento,
# deberá aplicar un descuento de 5.

# def descuento(precio, descuento=5):
#     costo = precio - descuento
#     print(f"Valor a pagar es {costo}")
#
#
# descuento(10)  # 5
# descuento(10, 2)  # 8


# funcion usando el return
# def usando_return(a, b):
#     return a + b
#
#
# suma = usando_return(10, 30)
# print(suma)

# Funciones anidadas o reutizacion de funciones

# Define una funcion que solicite el nombre de una persona y define
# otra funcion que solicite la edad al final imprime el nombre y la edad en la segunda
# funcion

#
# def nombre():
#     name = input("Cual es tu nombre: ")
#     return name
#
#
# def edad(name):
#     year = input("Cual es tu edad: ")
#     print(f"Hola mi nombre es {name} y tengo {year} años")
#
#
# name = nombre()
# edad(name)
# edad(nombre())

# Escribir una función que calcule el área de un círculo y otra
# que calcule el volumen de un cilindro usando la primera función.


# def area_circulo(radio):
#     pi = 3.14
#     return pi * radio ** 2
#
#
# def volumen_cilindro(radio, alto):
#     return area_circulo(area_circulo(radio) * alto)
#
# print(volumen_cilindro(5, 10))

# Escribir una función que reciba como parametros parametros (nombre, color, edad, genero, alias)
# y retorne un diccionario con esos datos y luego en otra funciona usando ese objeto
# imprime esos datos, recurda usar M = masculino y F = femenino
# Juan tiene 20 años,  le gusta el color rojo y todos "la / le" conocen como robotin.

# nombre = input("Ingrese un nombre: ")
# color = input("Ingrese un color: ")
# edad = input("Ingrese una edad: ")
# genero = input("Ingrese el genero: <M/F> ")
# alias = input("Ingrese el alias: ")
#
#
# def create_dic(nombre, color, edad, genero, alias):
#     return {
#         "nombre": nombre,
#         "color": color,
#         "edad": edad,
#         "genero": genero,
#         "alias": alias,
#     }
#
# def persona(dic):
#     genero = "la" if dic.get('genero') == "F" else "lo"
#     print(f"{dic['nombre']} tiene {dic['edad']} años,  le gusta el color {dic['color']}"
#           f" y todos {genero} conocen como {dic.get('alias')}.")
#
#
# persona(create_dic(nombre, color, edad, genero, alias))

# GLOBALES
# Local

# apellido = "Perez" # GLOBAL
#
# def a():
#     nombre = "Juan" # LOCAL
#     return nombre
#
#
# def b():
#     nombre_completo = nombre + apellido

# Yomiel hoy va comprar 2 pizzas ( 8 rebadas por pizza ) y queremos saber cuantas quedaron

# total_rebanadas = 2 * 8 # 16
#
#
# def cant_personas():
#     personas = 5
#     return personas
#
#
# def cant_rebanadas_x_persona():
#     rebanada_x_persona = 2
#
#     rebanadas_comidas = cant_personas() * rebanada_x_persona # 10
#     quedan = total_rebanadas - rebanadas_comidas # 16 - 10 = 6
#     print(f"Las rebanadas restantes son {quedan}")
#
# cant_rebanadas_x_persona()


# def persona(nombre, edad=18, color='blanco', ):
#     print(f"{nombre} tiene {edad} años, le gusta el color {color}.")
#
#
# persona("Andrea")
# persona("Andrea", color="ROJO" )
