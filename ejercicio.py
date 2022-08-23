# clase22-08-22

# Ejercicio práctico
#Una empresa de envios nos pide que calculemos el precio del envio elegido por 
# el usuario al final de una compra. Se sabe que el precio base del envío es $400, y se pueden elegir 2 tipos de envios:

# Opción 1: envío regular (10 días hábiles), con 15% de recarga.
# Opción 2: envío express (2 días hábiles), con 45% de recarga.

# Variables
opcion = 0
precio = 0

# CONSTANTES
BASE = 400 # tipo de dato entero
RECARGO_REGULAR = 0.1 # tipo de dato flotante
RECARGO_EXPRESS = 0.45 # tipo de dato flotante

# DATOS POR PANTALLA
print("Seleccione la opción de envio que desee ")
print("La base del envio es $" + str(BASE))
print("1 - Envio regular (10 días hábiles)\n2 - Envio express(2 días hábiles)")
# INGRESO POR PANTALLA
opcion = int(input("Ingrese el numero de opcción: "))

if ( opcion == 1):
  precio = BASE + (BASE * RECARGO_REGULAR)
  print("El envio cuesta $" + str(precio))
elif ( opcion == 2 ):
  precio = BASE + (BASE * RECARGO_EXPRESS)
  print("El envio cuesta $" + str(precio))
else:
  print("La opción elegida no está disponible")
