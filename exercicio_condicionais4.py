# Calculo Media de Nota - Gabriel Perencine
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media < 7:
    status = 'Reprovado!'
elif 7 <= media < 10:
    status = 'Aprovado!'
elif media == 10:
    status = 'Aprovado com distinção!'
else:
    status = 'ERRO: Nota inválida!'

print(f'\nMédia: {media:,.2f}')
print(status)