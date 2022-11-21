print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->' .format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('FIM!')    
print('Progressão finalizada com {} termos!' .format(total))