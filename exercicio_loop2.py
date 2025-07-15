# calculador de despesa - Gabriel Lima
qtd_despesas = int(input('Quantas compras foram feitas: '))
valor_total = 0

for i in range(qtd_despesas):
    valor = float(input(f'Qual o valor da compra {i+1}: R$ '))
    valor_total += valor

print(f'\nVocê gastou R${valor_total:,.2f} no total')