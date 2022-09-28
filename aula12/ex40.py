nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Você esta APROVADO')
elif media <= 4.9:
    print('Você esta REPROVADO')
else:
    print('Você ficou de RECUPERAÇÃO')    

print('Você tem media {}'.format(media))