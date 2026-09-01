#Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.


lista_original = []
for i in range (20):
    num = int(input('Digite um número'))
    lista_original.append(num)

for item in lista_original:
    if lista_original.count(item) > 1:
        lista_original.remove(item)

print(lista_original)



