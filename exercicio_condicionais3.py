# Calculo desconto de IR - Gabriel Perencine
salario_bruto = float(input('Digite seu sálario: '))

if 2000 < salario_bruto <= 3500:
    ir = 0.10
    salario_liquido = salario_bruto - (salario_bruto * ir)
elif 3500 < salario_bruto <= 5000:
    ir = 0.15
    salario_liquido = salario_bruto - (salario_bruto * ir)
elif 5000 < salario_bruto:
    ir = 0.20
    salario_liquido = salario_bruto - (salario_bruto * ir)
else:
    ir = 0
    salario_liquido = salario_bruto

print(f'\nSalário Bruto: R$ {salario_bruto:,.2f}\n'
      f'Desconto de IR: {ir*100}%\n'
      f'Sálari Líquido: R$ {salario_liquido:,.2f}')