#                 PARTE TEORICA
#def contador(i, f, p):
#    """Faz um contagem e mostra na tela

#    Args:
#        i : Indica o valor de inicio da contagem. 
#        f : Indica o valor para o final da contagem.
#        p : Indica o passo da contagem (de quanto em quanto que vai ocorrer a contagem).
#        return : Sem retorno
#    Exemplo: contador(1, 5, 1)
#            1 2 3 4 5    
#    """
#   c = i
#    while c <= f:
#        print(f'{c} ', end='')
#        c += p
#    print('FIM')
    
#contador(1, 5, 1)         

#help(contador)

#-----------------------------------------------------------

#def teste():
#    n1 = 4
#    print(f'N1 dentro vale {n1}')
#n1 = 8
#teste()
#print(f'N1 fora vale {n1}')    

#---------------------------------------------------------------

#def soma (a=0, b=0, c=0):
#    s = a + b + c
#    return s

#r1=soma(2, 4, 8)
#r2=soma(4, 8)
#r3=soma(4)

#print(f'Os resultados das somas foram {r1}, {r2} e {r3}')

#---------------------------------------------------------------

#         PARTE PRATICA

#def fatorial(num=1):
#    f = 1
#    for c in range (num, 0, -1):
#        f *= c
#    return f

#n = int(input('Digite um número: '))
#f1 = fatorial(5)
#f2 = fatorial(2)
#f3 = fatorial()
#print(f'O fatorial de {n} é igual ao {fatorial(n)}')    
#print(f'Os resultados do fatorial dos valores são {f1}, {f2}, {f3}')

#---------------------------------------------------------------

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
   
num = int(input('Digite um valor: ')) 
if par(num):
    print('É par')
else:
    print('É impar')       