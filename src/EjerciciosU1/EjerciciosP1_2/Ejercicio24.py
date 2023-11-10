precio=round((float(input("Introduce un precio con dos decimales: "))),2)

precio=str(precio).split(".")

print("El precio es ",int(precio[0])," euros y ",int(precio[1])," céntimos")