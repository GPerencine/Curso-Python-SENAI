# pedra papel ou tesouro - Gabriel Perencine
# NUNCA empata
import random
placar_jogador = 0
placar_pc = 0
jogar_dnv = ''

while True:
    if jogar_dnv == 'n':
        break

    while True:
        escolha_jogador = input("escolha pedra, papel ou tesoura: ").lower()
        if escolha_jogador == 'pedra' or escolha_jogador == 'papel' or escolha_jogador =='tesoura':
            break
        else:
            print('ERRO: Opção Inválida!')
            continue
    # match escolha_jogador:
    #     case 'pedra': jogador = 1
    #     case 'papel': jogador = 2
    #     case 'tesoura': jogador = 3
    #     case _:
    #         print('ERRO: Escolha Inválida!')
    #         continue

    while True:
        escolha_pc = random.choice(['pedra', 'papel', 'tesoura'])
    #     pc = random.randint(1, 3)
        if escolha_pc != escolha_jogador:
            break
        else:
            continue

    # match pc:
    #     case 1:
    #         escolha_pc = 'pedra'
    #     case 2:
    #         escolha_pc = 'papel'
    #     case 3:
    #         escolha_pc = 'tesoura'

    print(f"\nJogador : {escolha_jogador.title()}")
    print(f"Computador: {escolha_pc.title()}")

    if escolha_pc == 'pedra' and escolha_jogador == 'tesoura':
        print('COMPUTADOR VENCEU!')
        placar_pc += 1
    elif escolha_pc == 'papel' and escolha_jogador == 'pedra':
        print('COMPUTADOR VENCEU!')
        placar_pc += 1
    elif escolha_pc == 'tesoura' and escolha_jogador == 'papel':
        print('COMPUTADOR VENCEU!')
        placar_pc += 1

    if escolha_jogador == 'pedra' and escolha_pc == 'tesoura':
        print('JOGADOR VENCEU!')
        placar_jogador += 1
    elif escolha_jogador == 'papel' and escolha_pc == 'pedra':
        print('JOGADOR VENCEU!')
        placar_jogador += 1
    elif escolha_jogador == 'tesoura' and escolha_pc == 'papel':
        print('JOGADOR VENCEU!')
        placar_jogador += 1

    print(f'----------Placar----------\n'
          f'JOGADOR: {placar_jogador} X COMPUTADOR: {placar_pc}\n'
          f'--------------------------')

    while True:
        jogar_dnv = input('Quer jogar novamente? (s ou n) ').lower()
        if jogar_dnv == 's':
            print('')
            break
        elif jogar_dnv == 'n':
            break
        else:
            print('ERRO: Opção Inválida!')
            continue