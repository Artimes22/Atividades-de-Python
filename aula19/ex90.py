alunos = {}
alunos['Nome'] = str(input('Qual o nome do aluno: '))
alunos['Nota'] = float(input(f'Qual a nota do aluno {alunos["Nome"]}: '))
print('='*20) 
if alunos['Nota'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif alunos['Nota'] >= 5:
    alunos['Situação'] = 'Recuperação'
elif alunos['Nota'] < 5:
    alunos['Situação'] = 'Reprovado'
    
for k, v in alunos.items():
    print(f'- {k} é igual a {v}')    