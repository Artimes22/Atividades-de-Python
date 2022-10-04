print('{:=^40}' .format("LOJA"))
compra = float(input("Qual o valor da compra? R$ "))
pagamento = int(input('''
Qual o metodo de pagamento?
[1] A vista no dinheiro/cheque
[2] A vista no cartão
[3] 2X no cartão
[4] 3X ou mais no cartão
'''))

print('='*30)

if pagamento == 1:
    total = compra - (compra * 10 / 100)
elif pagamento == 2:
    total = compra - (compra * 5 / 100)
elif pagamento == 4:
    total = compra + (compra * 20 / 100)
    parcelas = int(input('Quantas parcelas quer que passe a compra? '))
    print('Sua compra ficou com {} parcelas de {:.2f}'.format(parcelas, (total / parcelas)))
elif pagamento == 3:
    total = compra
    print('Sua compra ficou com 2 parcelas de R$ {:.2f}'.format(compra / 2))
else:
    print("Opção INVALIDA tente novamente")

print('O valor final do produto ficou R$ {:.2f}'.format(total))
