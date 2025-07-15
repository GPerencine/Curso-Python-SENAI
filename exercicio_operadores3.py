nota1 = float(input('Nota 1° Bimestre: '))
nota2 = float(input('Nota 2° Bimestre: '))
nota3 = float(input('Nota 3° Bimestre: '))
nota4 = float(input('Nota 4° Bimestre: '))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 6:
    print(f"\nVocê passou!\n"
          f"Média: {media:.2f}")
else:
    print(f'\nReprovado!\n'
          f'Média: {media:.2f}')