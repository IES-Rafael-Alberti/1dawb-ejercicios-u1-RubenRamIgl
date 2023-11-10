importe=float(input("Introduce el importe sin IVA: "))
iva=int(input("Introduce el iva del producto: "))
valorIva=importe*iva/100
final=importe+valorIva
print("El precio final del artículo es ",final," euros")