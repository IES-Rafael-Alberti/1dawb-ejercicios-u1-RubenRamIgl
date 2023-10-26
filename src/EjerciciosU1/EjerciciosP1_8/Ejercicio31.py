#PSEUDOCÓDIGO
"""
Inicio
	Escribe "Introduce un número: "
	Lee num
	
	Mientras (num < 1 or num > 10)
		Escribe "Inténtalo otra vez! (1-10): "
		Lee num
	Escribe "Correcto!"
Fin
"""

num=int(input("Introduce un número: "))

while(num<1 or num>10):
    num=int(input(("Intétalo otra vez! (1-10): ")))

print("Correcto!")