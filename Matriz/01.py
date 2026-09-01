matriz = []
for i in range (4):
    linhas = []

    for j in range (4):
        num = int(input('Digite um número: '))
        linhas.append(num)
    matriz.append(linhas)


contador = 0
for linhas in matriz:
    for elemento in linhas:
        if elemento > 10:
            contador += 1 


print (contador)
