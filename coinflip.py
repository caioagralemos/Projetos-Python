import random
# coin flip app

moeda = ['cara', 'coroa']

resposta = []

quantidade = int(input("Quantidade de vezes que você quer girar a moeda: "))

cont = 0

while cont < quantidade:
    resposta.append(random.choice(moeda))
    cont += 1

caras = resposta.count('cara')
coroas = resposta.count('coroa')

if caras > coroas:
    porcentagem = round(((caras / quantidade) * 100), 2)
    print(f"A moeda caiu, em {porcentagem}% das vezes, cara.\nForam {caras} vezes cara e {coroas} vezes coroa.")
elif caras < coroas:
    porcentagem = round(((coroas / quantidade) * 100), 2)
    print(f"A moeda caiu, em {porcentagem}% das vezes, coroa.\nForam {coroas} vezes coroa e {caras} vezes cara.")
else:
    print(f"Empate!\nForam {coroas} vezes coroa e {caras} vezes cara.")