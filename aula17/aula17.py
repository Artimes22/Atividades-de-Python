#num = [2, 12, 6, 15, 10]
#num[2] = 7
#num.append(7)
#print(num)
#num.sort()
#print(num)
#num.sort(reverse=True)
#num.insert(2, 0)
#num.pop()
#print(num)
#print(f'Essa lista tem {len(num)} elementos ')

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1} encontramos o valor {v}')
    
    