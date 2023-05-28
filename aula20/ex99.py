def maior(* num):
    cont = 0
    maior =0
    print('\nAnalisando os valores informados... ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont ==0:
           maior = valor
        else:
           if valor > maior:
               maior = valor
        cont += 1 
    print(f'. Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado é {maior}')      
                  
       

maior(4, 5, 8, 2, 1, 7) 
maior(0, 10, 25, 8) 
maior(-2, -20, -12, -8, -1, -5)
maior(0)  