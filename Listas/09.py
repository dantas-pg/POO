import random 

lista = []
while len(lista) < 10:
    x = random.randint(0,50)
    if x not in lista:
        lista.append(x)

impares = [] 
for i in lista:
    if i % 2 != 0:
        impares.append(i)

print('Vetor 1:')
for i in range (0,len(lista),2):
    print(lista[i] , lista[i+1])

print('Vetor 2:')
for i in range (0,len(impares),2):
    if i + 1 < len(impares):
        print(impares[i], impares[i+1])
    else:
        print(impares[i])

