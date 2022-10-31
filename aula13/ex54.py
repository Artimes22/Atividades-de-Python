import datetime
atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for i in range (1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(i)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade' .format(totmaior))
print('E ao todo também tivemos {} pessoas menor de idade' .format(totmenor))            