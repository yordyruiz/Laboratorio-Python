#Paso 1: Crea una lista vacía llamada beatles.
#Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista:
# John Lennon, Paul McCartney y George Harrison





Beatles= []# paso 1
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")

print("Paso 2:", Beatles)

# paso 3
#Paso 3: Emplea el bucle for y el append() para pedirle al usuario que agregue 
# los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.

for i in Beatles:
    i= input("agrega a Stu Sutcliffe y Pete Best!: ")
    Beatles.append(i)
    if i == "Pete Best":
        break


print("Paso 3:", Beatles)

# paso 4
# Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.

print("Paso 4:", Beatles)

# paso 5
#Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))