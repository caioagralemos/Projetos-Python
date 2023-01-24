import random

# GERADOR DE NÚMEROS DA MEGA SENA!
# by Caio Agra Lemos

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n\nGERADOR DE NÚMEROS DA MEGA SENA!\nby Caio Agra Lemos\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
menu = input("Digite 1 para números aleatórios ou 2 para escolher os números máximos: ")

if menu == "1":
    um = random.randrange(60)
    dois = random.randrange(60)
    tres = random.randrange(60)
    quatro = random.randrange(60)
    cinco = random.randrange(60)
    seis = random.randrange(60)

    print(f"\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n\nSeus números da sorte são:\n{um} {dois} {tres} {quatro} {cinco} {seis}\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
elif menu == "2":
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n\nEscolha seus números máximos:\n")
    one = input("Número máximo da primeira marcação: ")
    one = int(one)
    two = input("Número máximo da segunda marcação: ")
    two = int(two)
    three = input("Número máximo da terceira marcação: ")
    three = int(three)
    four = input("Número máximo da quarta marcação: ")
    four = int(four)
    five = input("Número máximo da quinta marcação: ")
    five = int(five)
    six = input("Número máximo da sexta marcação: ")
    six = int(six)
    print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n")

    if (one <= 60 and two <= 60 and three <= 60 and four <= 60 and five <= 60 and six <= 60) :
        um = random.randrange(one)
        dois = random.randrange(two)
        tres = random.randrange(three)
        quatro = random.randrange(four)
        cinco = random.randrange(five)
        seis = random.randrange(six)
        print(f"Seus números da sorte são:\n{um} {dois} {tres} {quatro} {cinco} {seis}\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    else:
        print("Números inválidos!\nOs números devem todos ser menores ou iguais à 60.\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
else:
    print("Número inválido!\n")
    
input('Aperte ENTER para finalizar o aplicativo.')
