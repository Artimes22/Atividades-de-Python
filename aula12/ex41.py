from datetime import datetime
from operator import iadd

atual = datetime.today().year

nascimento = int(input('Qual o ano de nascimento do atleta: '))
idade = atual - nascimento
print('a idade do atleta é de {} anos' .format(idade))

if idade <= 9:
    print('Atleta MIRIN')
elif idade <= 14:
    print('Atleta INFANTIL')    
elif idade <= 19:
    print('Atleta JÚNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')     
elif idade > 25:
    print('Atleta MASTER')      