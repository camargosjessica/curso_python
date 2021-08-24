def jogar():
    print("Bem vindo ao jogo")

    palavra_secreta = "banana"
    acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(acertadas)

    while not acertou and not enforcou:

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                acertadas[index] = letra
            index = index + 1
        print(acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()