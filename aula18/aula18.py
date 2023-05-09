#teste = []
#teste.append('Gustavo')
#teste.append(40)

#galera= []
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1]=22
#galera.append(teste[:])

#print(galera)

#-----------------------------------------

#pessoal = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
#print(pessoal[0][0])
#print(pessoal[2][1])
#print(pessoal[3])
#print(pessoal[0][3])
#for p in pessoal:
#    print(f'{p[0]} tem {p[1]} anos de idade')
    
#--------------------------------------------------------- 

galera = []
dados = []
totmaior = totmenor = 0

for c in range (0, 3):
    dados.append(str(input(f'Qual o {c+1}º nome a ser adcionado: ')))
    dados.append(int(input(f'Qual a idade da {c+1}ª pessoa: ')))    
    galera.append(dados[:])
    dados.clear()
 
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
                
print(f'temos {totmaior} maiores de idade e {totmenor} menores de idade')                