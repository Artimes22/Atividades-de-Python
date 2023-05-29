def notas(*n, sit=False):
    """
       ->Função para analizar as notas e a situação de vários alunos.
    PARAM *n: uma ou mais notas dos alunos.
    PARAM sit: Valor opcional para ver se deve ou não mostrar a situação.
    Returns: dicionario com varias informações da turma.

    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'    
        else:
            r['Situação'] = 'RUIM'
    return r
    

#Programa pricipal
resp = notas(5.5, 2.5, 9, 8.5, 10, sit=True)
print(resp)