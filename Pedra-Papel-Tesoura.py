import random

def jogo(pontocpu, pontojogador):

    def fimdejogo(feedback):
        if feedback == "J" or feedback == "j":
            jogo(pontocpu, pontojogador)
        else:
            print("\nFim de Jogo!")
            if pontojogador > pontocpu:
                print(f"Você venceu!\nPlacar final:\nJogador: {pontojogador} CPU: {pontocpu}\n")
            elif pontojogador < pontocpu:
                print(f"Você perdeu!\nPlacar final:\nJogador: {pontojogador} CPU: {pontocpu}\n")
            else:
                print(f"Empate!\nPlacar final:\nJogador: {pontojogador} CPU: {pontocpu}\n")

    jogador = input("\nPressione (R) para pedra, (P) para papel ou (T) para tesoura: ")
    cpu = random.choice(["R", "P", "T"])
    print(f"Escolha do computador: {cpu}\n")
    if jogador == cpu:
        feedback = input(f"Empate!\nVocê tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou qualquer botão pra sair: ")
        fimdejogo(feedback)       
    elif jogador == "R" or jogador == "r":
        if cpu == "T":
            pontojogador += 1
            feedback = input(f"Pedra quebra a tesoura! :]\nPonto pra você! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)
        elif cpu == "P":
            pontocpu += 1
            feedback = input(f"Papel cobre a pedra :[\nPonto pra CPU! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)
    elif jogador == "P" or jogador == "p":
        if cpu == "R":
            pontojogador += 1
            feedback = input(f"Papel cobre a pedra :]\nPonto pra você! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)
        elif cpu == "T":
            pontocpu += 1
            feedback = input(f"Tesoura corta papel :[\nPonto pra CPU! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)
    elif jogador == "T" or jogador == "t":
        if cpu == "P":
            pontojogador += 1
            feedback = input(f"Tesoura corta papel :]\nPonto pra você! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)
        elif cpu == "R":
            feedback = input(f"Pedra quebra a tesoura! :[\nPonto pra CPU! Você tem {pontojogador} pontos e o computador tem {pontocpu} pontos.\nPressione (J) pra jogar novamente ou (S) pra sair: ")
            fimdejogo(feedback)


print("\n####################\n\nPEDRA, PAPEL E TESOURA\nby Caio Agra Lemos\n\n####################\n")
jogo(0,0)