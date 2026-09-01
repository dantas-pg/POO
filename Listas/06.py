#Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 0, 1 e 2 escreva uma mensagem informando que o código é inválido

lista = []
for i in range (5):
    num = int(input('Digite um número'))
    lista.append(num)

while True: 
    entrada = int(input('Digite um Código'))

    if entrada == '':
        print('Digite um codigo válido')
        continue
    codigo = entrada

    if codigo == 0: 
        print('Programa encerrado')
        break
    elif codigo == 1:
        print(lista)
    elif codigo == 2:
        lista.reverse()
        print(lista)
    else:
        print('Esse código é inválido')


