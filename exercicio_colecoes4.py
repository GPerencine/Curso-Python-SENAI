# estoque - Gabriel Perencine
estoque = {}
count = 1
while True:
    print('1 - Adicionar Produto\n'
          '2 - Consultar Produto\n'
          '3 - Alterar Preço\n'
          '4 - Remover Produto\n'
          '5 - Sair')

    escolha = int(input('Digite a operação que desejar: '))


    if escolha == 1:
        produto = input("\nProduto: ").title()
        info = []
        preco = float(input(f'Preço de {produto}: R$'))
        quantidade = int(input(f"Quantidade de {produto}: "))
        info.append(quantidade)
        info.append(f'{preco:,.2f}')
        estoque[produto] = info

    elif escolha == 2:
        consulta = input('\nQual produto você deseja consultar do estoque: ').title()
        for p, q in estoque.items():
            if p == consulta:
                print(f'\n{p}: {q[0]} unidades, valor unitário: R${q[1]}')

    elif escolha == 3:
        alterar = input('\nQual produto deseja alterar o preço: ').title()
        novo_preco = float(input('Novo preço: R$'))

        for p, q in estoque.items():
            if p == alterar:
                print(f'Valor unitário antigo de {p}: R${q[1]}')

        estoque[alterar][1] = (f'{novo_preco:,.2f}')

        for p, q in estoque.items():
            if p == alterar:
                print(f'Novo valor unitário de {p}: R${q[1]}')

    elif escolha == 4:
        excluir = input('\nDigite o nome do produto que deseja excluir: ').title()
        del estoque[excluir]
        print(f'{excluir} removido com sucesso!')

    elif escolha == 5: break
    else: print('\nERRO: Operação Inválida!')

for p, q in estoque.items():
    print(f'{count} - {p}: {q[0]} unidades, valor unitário: R${q[1]}')
    count += 1

