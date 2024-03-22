# Pedir al usuario que ingrese un texto
Texto = input (" Ingrese un texto ".lower())

# Pedir al usuario que ingrese las letras a buscar
Letra1=input (" Ingrese una letra: ".lower())
Letra2=input (" Ingrese una segunda letra: ".lower())
Letra3=input (" Ingrese una tercera letra: ".lower())

# Agregar las letras dadas por el ususario a una lista
list=[]
list.append(Letra1)
list.append(Letra2)
list.append(Letra3)

# Contar las letras repetidas en el texto
Contar=Texto.count(list[0])

# Mostrarle al usuario las letras repetidas
print(f"El numero de letras repetidas es de: {Contar}")

# Contar el numero de palabras en el texto
Palabras=Texto.split()
Num=len(Palabras)

# Mostrarle al usuario el numero de palabras en el texto
print(f"El numero de plabras en tu texto es: {Num}")

# Obtener la primera letra
Primera_letra = Texto[0]

# Obtener la última letra
Ultima_letra = Texto[-1]

# Mostrar los resultados
print(f"La primera letra del texto es: {Primera_letra}")
print(f"La última letra del texto es: {Ultima_letra}")

# Invertir el orden de las palabras
Invertido = Palabras[::-1]

# Unir las palabras nuevamente con espacios
Invertido = " ".join(Invertido)

# Mostrar el texto invertido
print(f"El texto invertido es: {Invertido}")