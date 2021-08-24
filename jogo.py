import alura_jogo_2
import alura_jogo_3

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Adivinhação (2) Forca")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando adivinhação")
        alura_jogo_2.jogar()
    elif jogo == 2:
        print("Jogando forca")
        alura_jogo_3.jogar()


if __name__ == "__main__":
    escolher_jogo()