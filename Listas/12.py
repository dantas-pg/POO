vetorA = []
vetorB = []
vetorC = []

print('Digite os valores de A:')
for i in range(10):
    num = int(input('Número:'))
    vetorA.append(num)
print('Digite os valores de B:')
for i in range(10):
    num = int(input('Número:'))
    vetorB.append(num)

for i in range (10):
    if i % 2 == 0:
        vetorC.append(vetorA[i])
    else:
        vetorC.append(vetorB[i])


print(vetorC)