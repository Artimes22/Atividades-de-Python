import time

primeiro = float(input('Primeiro valor: '))
segundo = float(input('Segundo valor: '))

opcao = 0
while opcao != 7:
    opcao = int(input('''O que você quer fazer com esses valores?
    [1] SOMAR
    [2] SUBTRAIR
    [3] MULTIPLICAR
    [4] DIVIDIR
    [5] MAIOR E MENOR
    [6] NOVOS VALORES
    [7] SAIR DO PROGRAMA
    '''))
    time.sleep(1)
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {:.2f} e {:.2f} é igual a {:.2f}' .format(primeiro, segundo, soma))
    elif opcao == 2:
        sub = primeiro - segundo
        print('A subtração entre {} e {} é igual a {}' .format(primeiro, segundo, sub))
    elif opcao == 3:
        mult = primeiro * segundo
        print('A multiplicação entre {} e {} é igual a {}' .format(primeiro, segundo, mult))   
    elif opcao == 4:
        div = primeiro / segundo
        print('O resultado entre a divisão de {} e {} é igual a {}' .format(primeiro, segundo, div))
    elif opcao == 5:
        if primeiro > segundo:
            print('O maior valor é {} e o menor é {}' .format(primeiro, segundo))
        else:
            print('O maior valor é {} e o menor é {}' .format(segundo, primeiro))    
    elif opcao == 6:
        primeiro = float(input('Informe um novo primeiro valor: '))
        segundo = float(input('Informe um novo segundo valor: '))
    time.sleep(1)
print('Fim do programa!')    