Texto = input (" Ingrese un texto ".lower())

Letra1=input (" Ingrese una letra: ".lower())
Letra2=input (" Ingrese una segunda letra: ".lower())
Letra3=input (" Ingrese una tercera letra: ".lower())

list=[]
list.append(Letra1)
list.append(Letra2)
list.append(Letra3)

Contar=Texto.count(list[0])

print(Contar)

Palabras=Texto.split()
Num=len(Palabras)

print(Num)
