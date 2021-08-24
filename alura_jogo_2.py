import random


def jogar():
    print("Bem vindo ao teste")

    numero_secreto = random.randrange(1, 31)
    total_tentativas = 0
    pontos = 100

    print("Escolha seu nível (1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_tentativas = 9
    elif nivel == 2:
        total_tentativas = 6
    else:
        total_tentativas = 3

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite seu número entre 1 e 30: ")
        print("Você digitou ", chute)
        numero = int(chute)

        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero == numero_secreto
        maior = numero > numero_secreto
        menor = numero < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto")
            perdidos = abs(numero_secreto - numero)
            pontos = pontos - perdidos

        print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
