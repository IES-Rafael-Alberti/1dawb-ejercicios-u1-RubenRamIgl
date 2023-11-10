frase=input("Introduce una frase: ")

vocal=input("Introduce una vocal en minúscula: ")

if vocal in "aeiou":
    fraseFinal=frase.replace(vocal,vocal.upper())
    print("La frase con la vocal en mayíuscula: ",fraseFinal)
else:
    print("Introduce una vocal en minúsculas correcta: ")
