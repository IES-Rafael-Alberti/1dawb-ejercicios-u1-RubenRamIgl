#PSEUDOCÓDIGO
"""
Inicio
	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x <= y) entonces
		numIni = x
		numFin = y
	Sino
		numIni = y
		numFin = x
		
	Mientras (numIni <= numFin) hacer
		Escribe numIni
		Si (numIni != numFin) entonces
			Escribe "-"
        numIni = numIni + 1
Fin
"""

x=int(input("Introduce un número: "))
y=int(input("Introduce otro: "))

if(x<=y):
    numIni=x
    numFin=y
else:
    numIni=y
    numFin=x

while(numIni<=numFin):
    print(numIni,end="")
    if(numIni!=numFin):
        print("-",end="")
    numIni=numIni+1