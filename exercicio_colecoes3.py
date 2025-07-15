# Dicionário - Gabriel Perencine

contatos = {}
count = 1

while True:
    nome = input('Digite o nome do contato: ').title()
    if nome:
        qte_num = int(input('Quantos numeros quer adicionar para essa pessoa: '))
        numeros = []
        for i in range(qte_num):
            num = input(f'Digite o número {i+1}: ')
            numeros.append(num)

        contatos[nome] = [numeros]
    else:
        break

print('\n---Lista de contatos---')
for nome, num in contatos.items():
    print(f'{count} - {nome}: {num} ')
    count += 1

count = 1
excluir = input('\nDigite o nome do contato que deseja excluir: ').title()
del contatos[excluir]
print(f'\nContato de {excluir} removido com sucesso!')


count = 1
mudar = input('\nDigite o nome do contato que deseja alterar o numero: ').title()
num_novo = input('Digite o novo numero: ')
contatos.update({mudar : num_novo})

print('\n---Lista de contatos---')
for nome, num in contatos.items():
    print(f'{count} - {nome}: {num} ')
    count += 1
