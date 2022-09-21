casa = float(input('Qual o preço da casa?'))
salario = float(input('Qual seu salario?'))
tempo = int(input('Em quantos anos você quer pagar o financiamento?'))

minimo = salario * 30 / 100
prestação = casa / (tempo * 12)

print('')
print('Para pagar uma casa no valor de {:.2f}, no periodo de {} anos' .format(casa, tempo))
print('O valor da prestação sera de R$ {:.2f}' .format(prestação))
print('')

if prestação <= minimo:
    print('O emprestimo foi CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')    
