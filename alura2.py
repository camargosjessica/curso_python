print("Bem vindo ao teste")

numero_secreto = 30
total_tentativas = 2
rodada = 1

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite seu número entre 1 e 100: ")
    print("Você digitou ", chute)
    numero = int(chute)

    if(numero < 1 or numero > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero == numero_secreto
    maior = numero > numero_secreto
    menor = numero < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")

    print("Fim do jogo!")