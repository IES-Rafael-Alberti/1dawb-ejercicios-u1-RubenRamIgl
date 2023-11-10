def calcularIva(importe,iva):
    valorIva=importe*iva/100
    final=importe+valorIva
    return ("El precio final del artículo es {:.2f} euros").format(final)

importe=float(input("Introduce el importe sin IVA: "))
iva=float(input("Introduce el iva del producto: "))

print(calcularIva(importe,iva))