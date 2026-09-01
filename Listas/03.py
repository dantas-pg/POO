#Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.#

lista = []
for i in range (5):
    num = int(input('Digite um número'))
    lista.append(num)

maior = lista.index(max(lista))
menor = lista.index(min(lista))

print(f'O maior se encontra na posição {maior} e o menor na posição {menor}')

                    