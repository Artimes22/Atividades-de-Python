lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'batata-frita')
#print(lanche[2:])
#print(lanche[-1])
#print(lanche[:3])
#print(lanche[2])
for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Na posição {pos} eu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
print('Eu comi para caramba!')    