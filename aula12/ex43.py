peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC desta pessoa é {:.2f}' .format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você esta com o PESO NORMAL') 
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta com OBESIDADE') 
else:
    print('Você esta com OBESIDADE MORBIDA, você precisa se cuidadar')               