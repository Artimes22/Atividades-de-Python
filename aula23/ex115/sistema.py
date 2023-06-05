import time
from lib.interface import *

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2') 
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!!')
        break 
    else:
        print('\033[31mERRO! digite um opção valida!\033[m')          
    time.sleep(1.2)