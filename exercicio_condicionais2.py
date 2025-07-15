# Tipo de Triangulo - Gabriel Perencine
lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado1 == lado3:
        print('\nTriângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('\nTriângulo Isóceles')
    else:
        print('\nTriângulo Escaleno')
else:
    print('\nInválido! Lados não fecham um triângulo!')