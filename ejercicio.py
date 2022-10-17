lista = ["1", 2, 3, 5, "camilo"]

print(lista[1])

lista[1] = "dos"

print(lista[1])

lista2dimensiones = [["Jonh","Doe"], [1,2,3]]

print(lista2dimensiones[0][1])

lista2dimensiones[0][1] = "Smith"

print(lista2dimensiones[0][1])

lista.append(6)

print(lista)

elementoEliminado = lista.pop(1)

print(lista)
print(elementoEliminado)

# INSERT

lista.insert(3, "leonel")
print(lista)

# EXTEND
lista2 = [7,"leonel"]

lista.extend(lista2)

print(lista)

# SORT
listaNom = ["gonzalo", "sol", "camilo", "hernan", "estú"]
listaLet = ["b", "a", "f", "c", "h"]
listaNum = [7,2,5,15,8,5,7]
listaNum.sort()
listaLet.sort()

print(listaNum)
print(listaLet)

for i in range(len(lista)):
  print(lista[i])
  
for elemento in lista:
  print(elemento)