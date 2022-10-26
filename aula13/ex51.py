print("="*25)
print(" 10 TERMOS DE UMA PA")
print("="*25)


termo = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão? "))
decimo = termo + (10-1) * razao
for i in range(termo, decimo + razao, razao):
    print (i, end='-> ')
print('ACABOU')