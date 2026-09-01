lista = list()
for i in range(10):  
    num = int(input('Digite um número: '))
    lista.append(num)

for indice in range(len(lista)):
    if lista[indice] < 0:
        lista[indice] = 0  
print(lista)
