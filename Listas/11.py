a = []
b = []
c = []

print('Digite os números de A:')
for i in range (10):
    num = int(input('Número:'))
    a.append(num)

print('Digite os números de B:')  
for i in range (10):
     num = int(input('Número:'))
     b.append(num)
###
for i in range(len(a)):
    num = a[i] - b[i]
    c.append(num)

print (c)

