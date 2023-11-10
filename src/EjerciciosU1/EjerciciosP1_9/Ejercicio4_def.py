def fahrenheit(celsius):
    return (celsius*9/5)+32

c1=float(input("Introduce una temperatura en grados celsius: "))
c2=float(input("Introduce una temperatura en grados celsius: "))

print("La temperatura en grados fahrenheit es: {:.2F}ºF({:.2F}ºC)".format(fahrenheit(),c1))
print("La temperatura en grados fahrenheit es: {:.2F}ºF({:.2F}ºC)".format(fahrenheit(),c2))