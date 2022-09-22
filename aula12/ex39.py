from datetime import datetime

atual = datetime.today().year
nascimento = int(input('Qual o seu ano de nacimento? '))

idade = atual - nascimento
print('Se você nasceu em {} então você tem {} anos no ano de {}' .format(nascimento, idade, atual) )
if idade < 18:
    saldo = 18 - idade
    print('Você presisa se alistar daqui a {} anos' .format(saldo))
elif idade == 18:
    print('Voce PRECISA se alistar esse ano')
else:
    saldo = idade - 18
    print('Voce ja deve ter se alistado ha {} anos' .format(saldo))        
