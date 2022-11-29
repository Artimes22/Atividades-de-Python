tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]? ')).upper() .strip() [0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1          
        if sexo == 'F' and idade < 20:
            totM20 += 1              
    continuar = ' '
    while continuar not in 'SsNn':    
        continuar = str(input('Quer cadastrar uma pessoa? [S/N] ')).upper() .strip() [0]
    if continuar == 'N':
        break
print(f'O total de pessoas maiores de 18 anos é {tot18}')
print(f'Ao total temos {totH} homens cadastrados. ') 
print(f'E temos o total de {totM20} mulheres com menos de 20 anos.  ')   
print('Acabou')           

        
'''
print(f'Pessoas cadastradas {contador}')
print(f'Mulheres cadastradas {mulher}')'''