sexo = str(input("Qual seu sexo? ")) .strip().upper() [0]
while sexo in 'MmFf':
    sexo = str(input("Informe um valor valido: ")) .strip().upper() [0]
print("Sexo {} registrado com suceso" .format(sexo))    
