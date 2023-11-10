total=float(input("Introduce el precio completo del producto: "))
valorIva=total*10/100
valorProducto=total-valorIva

print("El IVA pagado (10%) es de ",round(valorIva,2)," euros, y el importe sin IVA es de "
      ,round(valorProducto,2)," euros")