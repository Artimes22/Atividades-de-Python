import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acesseível no momento') 
else:
    print('Consegui acessar o site pudim com sucesso')       