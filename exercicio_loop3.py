# Simulador de banco - Gabriel Perencine

saldo = 0

while True:
    print('1: Depósito\n2: Saque\ns: Sair')
    print(f'\nSaldo atual: R${saldo}')
    operacao = input('\nDigite a operação: ')
    if operacao == '1':
        deposito = float(input('\nQuanto quer depositar: '))
        saldo += deposito
        continue
    elif operacao == '2':
        saque = float(input('\nQuanto quer sacar: '))
        if saldo > saque:
            saldo -= saque
            continue
        else:
            print('\nERRO: Você não possui esse valor na conta!\n')
            continue
    elif operacao == 's':
        break
    else:
        print('\nERRO: Operação inválida!\n')

print(f'\nSeu saldo é de: R${saldo:,.2f}')