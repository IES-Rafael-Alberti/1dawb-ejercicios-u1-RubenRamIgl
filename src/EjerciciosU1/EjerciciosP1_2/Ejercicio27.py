nombre=input("Introduce el nombre del producto: ")
precio=float(input("Introduce el precio del producto: "))
unidades=int(input("Introduce el número de unidades: "))

precioTotal=float(precio*unidades)

print("Los dígitos vacíos aparecerán como 0")
print("{} Precio: {:0>9,.2f} Número de unidades: {:0>3} Precio total: {:0>11,.2f}".format(nombre,precio,unidades,precioTotal))