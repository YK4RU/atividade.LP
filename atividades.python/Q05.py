aluno = input('Nome do aluno: ')
matéria = input('Informe a matéria: ')
nota = float(input('Informe a nota: '))

if nota >= 5.5 and nota < 6:
    nota = 6  
if nota >= 6 and nota <= 10:
    print(f'{aluno} está aprovado em {matéria} com nota {nota}')
elif nota < 5.5 and nota >0:
    print(f'{aluno} está reprovado em {matéria} com nota {nota}')
else:
    print('Nota inválida, tente novamente.')