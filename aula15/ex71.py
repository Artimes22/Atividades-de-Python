print('-=' * 15)
print('{:^30}' .format('BANCO CEV'))
print('-=' * 15 ) 
valor = int(input('Qual o valor que você quer sacar? R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'total de {totalcedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10    
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break    
           
print('=' * 30)
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')           