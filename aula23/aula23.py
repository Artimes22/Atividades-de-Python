try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('\033[0;31mTivemos um problema com o tipo de dados informados. \033[m')
except ZeroDivisionError:
    print('\033[0;31mNão é posivel dividir um número por ZERO. \033[m')
except KeyboardInterrupt:
    print('\033[0;31mO usuario preferio não informar os dados> \033[m')         
   
else:        
    print(f'O resultado é {r:.2f} ')
finally:
    print('Muito obrigado. Volte sempre!')    