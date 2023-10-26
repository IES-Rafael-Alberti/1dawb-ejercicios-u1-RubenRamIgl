telefono=input("Introduce un número de teléfono con un prefijo y una extensión (+prefijo-numero-extension): ")

partesTelefono=telefono.split("-")
print("El teléfono sin prefijo ni extensión es: ",partesTelefono[1])