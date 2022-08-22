salario = float(input('Qual o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15) / 100
if salario > 1250:
    novo = salario + (salario * 10) / 100
print('Quem ganhava R$ {:.2f} vai passara ganhar R$ {:.2f} ' .format(salario, novo))    

