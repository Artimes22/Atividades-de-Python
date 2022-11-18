print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->' .format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')