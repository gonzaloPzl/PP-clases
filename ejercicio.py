mas_rapida = 0
mas_lenta = 0
promedio_de_vel = 0
tiempo_vuelta = 0
cant_vueltas = 0
acumulador_tiempos = 0

while(tiempo_vuelta >= 0):
  print("Ingrese el tiempo de la vuelta")
  tiempo_vuelta = float(input())
  if(tiempo_vuelta < 0):
    break
  acumulador_tiempos += tiempo_vuelta

  if (cant_vueltas == 0):
    mas_lenta = tiempo_vuelta
    mas_rapida = tiempo_vuelta
  
  if(cant_vueltas > 0):
    if(tiempo_vuelta < mas_rapida):
      tiempo_vuelta = mas_rapida
    if(tiempo_vuelta > mas_lenta):
      tiempo_vuelta = mas_lenta
  
  cant_vueltas += 1

print("La cantidad de vueltas fueron " + str(cant_vueltas))
print("La vuelta más rápida fue de " + str(mas_rapida) + " segundos")
print("La vuelta más lenta fue de " + str(mas_lenta) + " segundos")
print("El promedio de tiempo por vuelta es de " + str(acumulador_tiempos/cant_vueltas) + " segundos")