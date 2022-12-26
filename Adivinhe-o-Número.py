import random

def guess(x):
    numero = random.randint(1,x)
    guess = int(input(f"\nChute um número de 1 a {x}: "))
    tentativas = 0
    while guess != numero:
        if guess > numero:
            guess = int(input("Meu número é menor que isso! Tente novamente: "))
            tentativas += 1
        elif guess < numero:
            guess = int(input("Meu número é maior que isso! Tente novamente: "))
            tentativas += 1
    print(f"\nParabéns! Você descobriu meu número!\nNúmero de tentativas: {tentativas}\n")

def cpu_guess(x):
    low = 1
    high = x
    feedback = ''
    tentativas = 1
    while feedback != "c":
        guess = random.randint(low + 1, high - 1)
        feedback = input(f"\n\nEu adivinhei o número {guess}.\nPressione (C) se eu tiver acertado, (L) se o número for menor que isso, ou (H) se o número for maior que isso: ")
        if feedback == "l" or feedback == "L":
            high = guess
            tentativas += 1
        if feedback == "h" or feedback == "H":
            low = guess
            tentativas += 1
        if feedback == "C":
            break
    print(f"\nAcertei! Precisei de {tentativas} tentativas.\n")

print("\n####################\n\nADIVINHE O NÚMERO\nby Caio Agra Lemos\n\n####################\n\n")
opcao = input("Pressione:\n- 1 para adivinhar o número do CPU\n- 2 para o CPU advinhar seu número\n\n")

# adivinhar o número da CPU
if (opcao == "1"):
    guess(100)
# CPU advinhar seu número
elif(opcao == "2"):
    cpu_guess(100)
else:
    print("\nOpção inválida!\n")

print("Pressione qualquer botão pra encerrar o programa\n")