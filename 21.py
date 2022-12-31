import random

print("\n#####################\n\n21 - the game\nby Caio Agra Lemos")


def vinteeum(pontosjogador, pontoscpu):
    pcjogador = random.randint(1,10)
    pccpu = random.randint(1,10)
    jogadorpassou = False
    cpupassou = False

    print(f"\n#####################\n\nO seu primeiro número é {pcjogador}, e o computador sabe disso.")
    print (f"A primeira carta da CPU é {pccpu}.\n")
    while pccpu <= 11:
        pccpu = pccpu + random.randint(1,10)
    if pccpu == 21:
        pass
    elif pccpu > 12 and pccpu < 16:
        chance = random.choice(["S", "N"])
        if chance == "S":
            pccpu = pccpu + random.randint(1,10)
    elif pccpu > 15 and pccpu < 19:
        chance = random.choice(["S", "N", "N", "N", "N"])
        if chance == "S":
            pccpu = pccpu + random.randint(1,10)
    if pccpu > 21:
        cpupassou = True

    feedback = input("Pressione (P) para puxar outra carta ou qualquer outra tecla para parar: ").upper()

    while feedback == "P":
        novacarta = random.randint(1,10)
        pcjogador = pcjogador + novacarta
        if pcjogador > 21:
            print(f"Sua nova carta é {novacarta} e seu novo total é {pcjogador}\n")
            jogadorpassou = True
            break
        else:
            print(f"Sua nova carta é {novacarta} e seu novo total é {pcjogador}\n")
            feedback = input("Pressione (P) para puxar outra carta ou qualquer outra tecla para parar: ").upper()

    print("O jogo está parado!\nVocê e seu oponente já puxaram todas as cartas.\n")

    def final(pontosjogador, pontoscpu):
        print("\n#####################\n\nFim de jogo!")
        if pontosjogador > pontoscpu:
            print("Você venceu!")
        elif pontosjogador < pontoscpu:
            print("Você perdeu!")
        else:
            print("Empate!")
        print(f"Placar final:\nJogador {pontosjogador} x CPU {pontoscpu}\n\n#####################\n")
    if jogadorpassou == False and cpupassou == False:
        if pcjogador > pccpu:
            pontosjogador += 1
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nPonto para você! :]\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)
        elif pcjogador < pccpu:
            pontoscpu += 1
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nPonto para a CPU :[\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)
        else:
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nEmpate.\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)
    elif jogadorpassou == False and cpupassou == True:
        pontosjogador += 1
        resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nA CPU passou! Ponto pra você. :]\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
        if resposta == "P":
            vinteeum(pontosjogador, pontoscpu)
        else:
            final(pontosjogador, pontoscpu)
    elif jogadorpassou == True and cpupassou == False:
        pontoscpu += 1
        resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nVocê passou! Ponto pra CPU.\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
        if resposta == "P":
            vinteeum(pontosjogador, pontoscpu)
        else:
            final(pontosjogador, pontoscpu)
    elif jogadorpassou == True and cpupassou == True:
        if pcjogador < pccpu:
            pontosjogador += 1
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nOs dois passaram, mas o seu foi menor! Ponto para você! :]\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)
        elif pcjogador > pccpu:
            pontoscpu += 1
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nOs dois passaram, mas o seu foi maior! Ponto para a CPU :[\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)
        else:
            resposta = input(f"Seu número é {pcjogador} e o da CPU é {pccpu}.\nEmpate.\n\nPressione (P) para jogar novamente ou qualquer botão para terminar a partida: ").upper()
            if resposta == "P":
                vinteeum(pontosjogador, pontoscpu)
            else:
                final(pontosjogador, pontoscpu)

vinteeum(0, 0)