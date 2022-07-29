hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
new_number = int(input("Reemplaze el nro central por un nro nuevo: "))
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list [2] = new_number
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista existente es: ", len(hat_list))
print(hat_list)


#METODOS PARA AGREGAR UN NRO A LA LISTA
#append() e insert()
#EJEMPLO

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(numbers)

#Agregando elementos a una lista: continuación
#APPEND
#Será una secuencia de números
#enteros consecutivos del 1 (luego agrega uno a todos los valores agregados) hasta 5.

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


#DISTINTO CODIGO: HACE LO CONTRARIO
#Deberías obtener la misma secuencia, pero en orden inverso (este es el mérito de usar el método insert()).


my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

