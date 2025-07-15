alunos = []

while True:
    nome = input('Digite o nome do aluno(enter para sair): ')
    if not nome:
        break

    idade = int(input('Digite a idade do aluno: '))
    notas = []
    qtd = int(input('Quantas notas quer digitar: '))
    for i in range(qtd):
        nota = float(input(f'Nota {i+1}: '))
        notas.append(nota)

    aluno = {
        'nome' : nome,
        'idade' : idade,
        'notas' : notas
    }
    alunos.append(aluno)
    print()

for aluno in alunos:
    media = sum(aluno['notas']) / len(aluno['notas'])
    aluno['media'] = media

print("\n---Médias dos alunos---")
for aluno in alunos:
    print(f'{aluno["nome"]}: média = {aluno["media"]:.2f}')

maior_media = {'nome' : '', 'media' : 0}

for aluno in alunos:
    if aluno['media'] > maior_media['media']:
        maior_media['nome'] = aluno['nome']
        maior_media['media'] = aluno['media']
print()
print(maior_media)
print()
for aluno in alunos:
    if aluno['media'] >= 7:
        print(aluno['nome'])