# Calculo IMC - Gabriel Perencine
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / (altura ** 2)

print(f'\nSeu IMC é: {imc:,.2f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está acima do peso!')
else:
    print('Você está obeso!')