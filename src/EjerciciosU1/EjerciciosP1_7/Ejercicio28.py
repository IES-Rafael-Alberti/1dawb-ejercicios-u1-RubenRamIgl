n1=int(input("Introduce el primer número: "))
n2=int(input("Introduce el segundo número: "))

while(n1==n2):
    print("Los números no pueden ser iguales")
    n1=int(input("Introduce el primer número: "))
    n2=int(input("Introduce el segundo número: "))

if(n1>n2):
    print("El número mayor es el ",n1," y entre ellos existen",n1-n2," números enteros")
elif(n1<n2):
    print("El número mayor es el ",n2," y entre ellos existen",n2-n1," números enteros")

#PSEUDOCÓDIGO
"""
inicio
	escribe "Introduce el primer número"
    lee n1
	escribe "Introduce el segundo número"
	lee n2
	mientras(n1==n2) hacer
		escribe "Los números no pueden ser iguales: "
		escribe "Introduce el primer número"
        lee n1
		escribe "Introduce el segundo número"
		lee n2
	si(n1>n2) entonces
		escribe "El número mayor es el "+n1+" y entre ellos existen"+(n1-n2)+" números enteros"
	si(n2<n2) entonces
		escribe "El número mayor es el "+n2+" y entre ellos existen"+(n2-n1)+" números enteros"
fin
"""