#pessoas = {'Nome': 'Artimes', 'Idade': 23, 'Sexo': 'M'}
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#pessoas['Peso'] = 68.8
#for v in pessoas.values():
#    print(v)
#print('-=-=-=-=-=')
#for k in pessoas.keys():    
#    print(k)
#print('-=-=-=-=-=')
#for i, n in pessoas.items():
#    print(f'{i} = {n}')    

#--------------------------------------------------------------------------#

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(estado1)
#print(estado2)
#print(brasil)
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

#==========================================================================#

estado = {}
brasil = []

for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)    

print('-='*20)


    