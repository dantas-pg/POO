#Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média dos valores.

lista = []
for i in range (5):
    num = int(input('Digite um número'))
    lista.append(num)

print(lista)
print(max(lista))
print(min(lista))
print(sum(lista)/len(lista))
      