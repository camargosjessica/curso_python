print("Bem vindo ao teste")

numero_secreto = 30
total_tentativas = 2
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite seu número: ")
    print("Você digitou ", chute)
    numero = int(chute)

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

    rodada = rodada + 1

    print("Fim do jogo!")