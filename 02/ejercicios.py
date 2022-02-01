# Ejercios
# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.
# cursos = []
#
# while (True):
#     curso = input("ingrese una asignatura: ")
#     cursos.append(curso)
#
#     continuar = input("Continuar <S/N> :")
#     if (continuar == "N"):
#         break
#
# print(cursos)

# 5
# 02
# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada
# una des las asignaturas de la lista y <nota> cada una de las
# correspondientes notas introducidas por el usuario.

# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# passed = []
#
# for subject in subjects:
#     score = float(input(f"Que nota has sacado en {subject} ?"))
#     if score > 5:
#         passed.append(subject)

# 03
# Escribir un programa que pregunte al usuario los números
# ganadores de la lotería primitiva, los almacene en una
# lista y los muestre por pantalla ordenados de menor a mayor.

# numeros = []
# for i in range(5):
#     numeros.append(int(input("Ingrese el numero ganador: ")))
#
# numeros.sort()
#
# print(f"Los numero ganadores son {numeros}")

# 04
# Escribir un programa que almacene en una lista los números del
# 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for i in range(1, len(numeros)+1):
# for i in range(1, 11):
#     print(numeros[-i], end=", ")

# No usar SORT
# Escribir un programa que almacene en una lista los siguientes precios,
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# precios = [50, 75, 46, 22, 80, 65, 8, 12, ]
# # None
# min = max = precios[0]  # esciling
#
# for precio in precios:  # desconocemos el tamaño (dinamico )
#     if precio < min:
#         min = precio
#     elif precio > max:
#         max = precio
#
#
# print("El minimo es " + str(min))
# print("El maximo es " + str(max))

# 04 Palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.

word = input("Ingrese una palabra: ")
revesed_word = word
word = list(word)
revesed_word = list(revesed_word)
revesed_word.reverse()

if word == revesed_word:
    print("Palindromo")
else :
    print("No es palindromo")


# 05 Escribir un programa que pida al usuario una palabra y muestre por
# pantalla el número de veces que contiene cada vocal.


