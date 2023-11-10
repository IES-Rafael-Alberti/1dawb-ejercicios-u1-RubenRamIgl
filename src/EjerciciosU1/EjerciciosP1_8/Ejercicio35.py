#PSEUDOCÓDIGO
"""
Inicio
	Escribe "Introduce dos números: "
	Lee n1
	Lee n2
	
	opcion = 0
	Mientras (opcion < 1 or opcion > 4) hacer
		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
		Lee opcion
		Si (opcion < 1 or opcion > 4) entonces
			Escribe "Error - No es una opción correcta (1-4)"
	
	Segun (opcion) entonces
		1:
			Escribe n1 + " + " + n2 + " = " + (n1+n2)
		2:
			Escribe n1 + " - " + n2 + " = " + (n1-n2)
		3:
			Escribe n1 + " * " + n2 + " = " + (n1*n2)
		4:
			Si (n2 == 0) entonces
				Escribe "La división por cero no es posible"
			Sino
				Escribe n1 + " / " + n2 + " = " + (n1/n2)
Fin
"""

print("Escribe dos números: ")
n1=int(input())
n2=int(input())

opcion=0

while(opcion<1 or opcion>4):
    opcion=int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "))
    if(opcion<1 or opcion>4):
        print("Error - No es una opción correcta (1-4)")

match(opcion):
    case 1:
        print(n1," + ",n2," = ",(n1+n2))
    case 2:
        print(n1," - ",n2," = ",(n1-n2))
    case 3:
        print(n1," * ",n2," = ",(n1*n2))
    case 4:
        if(n2==0):
            print("La división por cero no es posible")
        else:
            print(n1," / ",n2," = ",(n1/n2))