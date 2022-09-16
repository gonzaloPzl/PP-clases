print("Ingrese un numero para realizar la sumatoria")
sumando = int(input())
sumatoria = 0

for i in range(1, sumando + 1):
  sumatoria += i

print("La sumatoria de " + str(sumando) +" es " + str(sumatoria))


