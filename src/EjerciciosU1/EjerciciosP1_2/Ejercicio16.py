pan=int(input("Introduce una cantidad de barras de pan: "))

PRECIO=3.49

precioInicial=PRECIO*pan

descuento=float((precioInicial)*0.60)

precioFinal=float((3.49*pan)-descuento)

print("El precio de las barras de pan es {:.2f} su descuento es {:.2f} y su precio final es {:.2f}"
      .format(precioInicial,descuento,precioFinal))