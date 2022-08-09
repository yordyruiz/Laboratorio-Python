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

#Calcular la  SUMA de todos los valores almacenados en la lista my_list.
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)



#segundo aspecto de for
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)


#Pregunta: ¿Cómo se pueden intercambiar los valores de dos variables?

variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

#Imagina que necesitas reorganizar los elementos de una lista, es decir, revertir el orden de los elementos: 
#el primero y el quinto, así como el segundo y cuarto elementos serán intercambiados. El tercero permanecerá intacto.

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

#FUNCIONA CON MAS DE 100 ELEMENTOS? MM
#UTILIZAMOS EL BUCLE FOR PARA ESO ;)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)
#Hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto).
for i in range(length // 2):  #(esto funciona bien para listas con longitudes pares e impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto)
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
#Hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length-i-1) (desde el final de la lista);
print(my_list)

#en nuestro ejemplo, for i igual a 0 a la (length-i-1) da 4; for i igual a 3, da 3: esto es exactamente lo que necesitábamos
