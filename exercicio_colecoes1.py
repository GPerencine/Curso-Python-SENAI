# Lista de Frutas - Gabriel Perencine
lista = []
count = 0

for i in range (5):
    fruta = input("Digite uma fruta: ").title()
    lista.append(fruta)

print(f'\nPrimeira fruta: {lista[0]}\n'
      f'Última fruta: {lista[-1]}\n')

print('Lista com 5 frutas')
print(lista)

print('\nDigite 3 novas frutas')
for i in range (3):
    fruta = input("Digite uma fruta: ").title()
    lista.append(fruta)

print('\nLista com 8 frutas:')
print(lista)

print('\nRemovendo segundo item da lista:')
lista.remove(lista[1])
print(lista)

print('\nLista em ordem alfabética:')
lista.sort()
print(lista)

for i in lista:
    if i == 'Banana':
        count += 1

print(f'\nA fruta Banana aparece {count} vezes')
