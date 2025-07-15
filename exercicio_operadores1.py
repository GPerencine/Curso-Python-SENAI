raio = int(input('Digite o raio da cicunferência em cm: '))

area = 3.14 * raio ** 2
perimetro = 2 * 3.14 * raio
diametro = raio * 2

print(f'Área da Circunferência: {area:,.2f}cm²\n'
      f'Perímetro da Circunferência: {perimetro:,.2f}cm\n'
      f'Diâmetro da Circunferência: {diametro:,.2f}cm')