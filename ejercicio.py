caja = 5000
extraccion = 0
total_extracciones= 0
cantidad_extracciones = 0

while (caja > extraccion):
  print("Ingrese el monto de la extraccion")
  extraccion = int(input())
  if(caja > extraccion):
    caja -= extraccion
    total_extracciones += extraccion
    cantidad_extracciones += 1
    extraccion = 0

print("La cantidad sobrante en caja es $" + str(caja))
print("El monto total extraido es $" + str(total_extracciones))
print("La cantidad de extracciones es " + str(cantidad_extracciones))