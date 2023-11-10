nombre=input("Introduce tu nombre: ")
edad=int(input("Introude tu edad: "))

while(edad<0 or edad>125):
    print("Introduce una edad entre 0 y 125")
    edad=int(input("Introude tu edad: "))

if(nombre==""):
    nombre="Desconocido"

print("Te llamas ",nombre," y tienes edad ",edad,"te quedan ",125-edad," por cumplir")

#PSEUDOCÓDIGO
"""
inicio
	escribe "introduce tu nombre"
	lee nombre
	escribe "introduce tu edad"
	lee edad
	mientras(edad<0 or edad>125)hacer
		escribe "Introduce un número entre 0 y 125"
		escribe "introduce tu edad"
		lee edad
	si(nombre=="") entonces
		nombre="Desconocido"
	escribe ""Te llamas "+nombre+" y tienes edad "+edad+"te quedan "+(125-edad)+" por cumplir"
fin
"""