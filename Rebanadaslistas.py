# Copiando la lista entera.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#Así es como los índices negativos funcionan en las rebanadas:

#my_list[start:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#Si start especifica un elemento que se encuentra más allá del descrito por end
#  (desde el punto de vista inicial de la lista), la rebanada estará vacía:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

#La salida del fragmento es: []


#Si omites el start en tu rebanada, se supone que deseas obtener un segmento que 
# comienza en el elemento con índice 0.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

#Es por esto que su salida es: [10, 8, 6].

#Del mismo modo, si omites el end en tu rebanada,
#se supone que deseas que el segmento termine en el elemento con el índice:
#len(my_list).
#my_list[start:]
# es un equivalente mas compacto que: 
#my_list[start:len(my_list)]


my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)


#el omitir el inicio y fin crea una copia de toda la lista:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

#El resultado del fragmento es: [10, 8, 6, 4, 2]
#del
#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez,
#también puede eliminar rebanadas:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#La salida del fragmento es: [10, 4, 2].

#CUIDADO!!! VER
my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

#La instrucción del eliminará la lista, no su contenido.

