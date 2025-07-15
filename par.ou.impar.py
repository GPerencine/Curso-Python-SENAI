import random

while True:
    escolha_jogador = input("escolha par ou impar: ")
    escolha_computador = "impar" if escolha_jogador == "par" else "par"

    numero_computador = random.randint(0, 100)
    numero_jogador = int(input("Escolha um numero de 0 a 100: "))

    total = numero_jogador + numero_computador

    print(f"\nJogador : {numero_jogador}")
    print(f"Computador: {numero_computador}")
    print(f"Total: {total}")

    if escolha_jogador == "par" and total % 2== 0:
        print("JOGADOR VENCEU!")
    if escolha_jogador == "par" and total % 2!= 0:
        print("COMPUTADOR VENCEU!")
    if escolha_jogador == "impar" and total % 2 == 0:
        print("COMPUTADOR VENCEU!")
    if escolha_jogador == "impar" and total % 2 != 0:
        print("JOGADOR VENCEU!")

    jogar_dnv = input('Quer jogar novamente? (s ou n)')
    if jogar_dnv == 'n':
        break
