salario = float(input("qual o salario do funcionario? "))
reajuste = salario+salario*15/100
print("O salario de R${:.2f} com reajuste de 15% é igual a R${:.2f} ".format(salario, reajuste))