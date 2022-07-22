#Diseña un programa que use un bucle while y le pida continuamente al usuario que 
# ingrese una palabra a menos que ingrese "chupacabra" como la palabra de salida secreta, 
# en cuyo caso el mensaje "¡Has dejado el bucle con éxito". Debe imprimirse en la pantalla 
# y el bucle debe terminar.

palabraSecreta = "chupacabra"
palabraIngresada = input("Ingrese la palabra clave para salir del bucle: ")

while palabraIngresada != palabraSecreta:
    if palabraIngresada == palabraSecreta:
        break
    palabraIngresada = input("Ingrese la palabra clave para salir del bucle: ")
print("¡Has dejado el bucle con éxito")
