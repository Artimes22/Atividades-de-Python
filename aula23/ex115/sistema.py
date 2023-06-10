import time
from lib.interface import *
from lib.arquivo import *


arq = 'aula23/ex115/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
         

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar uma nova pessoa!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!!')
        break 
    else:
        print('\033[31mERRO! digite um opção valida!\033[m')          
    time.sleep(1.2)