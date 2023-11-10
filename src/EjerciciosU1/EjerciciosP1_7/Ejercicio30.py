n1=int(input("Introduce un número: "))
n2=int(input("Introduce hasta qué número imprimir: "))
n3=int(input("Introduce un incremento: "))

cont=n1

while (n1<0 or n2<0):
    if n1<0:
        print("El primer número debe ser mayor a 0")
        n1=int(input("Introduce un número: "))
        cont=n1
    if n2<0:
        print("El segundo número debe ser mayor a 0")
        n2=int(input("Introduce hasta qué número imprimir: "))

while(cont<=n2):
    if(cont<n2):
        print(cont,end="-")
    else:
        print(cont,end="")
    cont=cont+n3
    
#Si el último incremento supera n2, imprime n2 con un mensaje
if(cont>n2):
            print(n2,"(El contador Supera la serie)",end="")
        
#PSEUDOCÓDIGO
"""
inicio
	escribe "Introduce un número"
	lee n1
	escribe "Introduce hasta qué número imprimir"
	lee n2
    Escribe "Introduce un incremento: "
    lee n3
	cont=n1
    escribe "
	mientras(n1<0 or n2<0) hacer
		si(n1<0) entonces
			escribe "El primer número debe ser mayor a 0"
			escribe "Introduce un número"
			lee n1
			cont=n1
		si(n2<0) entonces
			escribe "El segundo número debe ser mayo a 0"
			escribe "Introduce hasta qué número imprimir"
			lee n2
	mientras(cont<=2) hacer
		si(cont<n2) entonces
			escribe cont+end="-"
		sino
			escribe cont+end=""
        cont=cont+n3
    si(cont>n2) entonces
		escribe n2+"(El contador Supera la serie)"
fin
"""