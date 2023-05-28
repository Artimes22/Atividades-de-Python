#---------------------------------OBRIGATORIEDADE DO VOTO----------------------------#

def voto(ano):
    from datetime import datetime
    atual = datetime.now().year 
    idade = atual - ano
    if idade < 16:
        return f'Você tem {idade} anos, NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Você tem {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Você tem {idade} anos, seu voto é OBRIGATORIO.'
        
nasc = int(input('Qual ano de nascimento: '))    

print(voto(nasc))