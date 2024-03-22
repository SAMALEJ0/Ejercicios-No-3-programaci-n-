Texto = input (" Ingrese un texto ".lower())
Letra1 = input (" Ingrese una letra ".lower())
Letra2 = input (" Ingrese una segunda letra ".lower())
Letra3 = input (" Ingrese una tercera letra ".lower())

list=(Letra1+Letra2+Letra3).lower()

Contar=(Texto.lower()).count(list)

print(Contar)
