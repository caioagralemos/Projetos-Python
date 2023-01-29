import datetime

while True:
    operacao = input("Digite som pra soma ou sub pra subtração: ")
    if operacao == "sub" or operacao == "som":
        break

if operacao == "sub":
    try:
        dt1_h = int(input("Data a subtrair (hora): "))
        dt1_m = int(input("Data a subtrair (minutos): "))
        dt1_s = int(input("Data a subtrair (segundos): "))
        dt1 = datetime.timedelta(hours=dt1_h, minutes=dt1_m, seconds=dt1_s)
        print("Primeira data recebida com sucesso.")
        dt2_h = int(input("Data a ser subtraída (hora): "))
        dt2_m = int(input("Data a ser subtraída (minutos): "))
        dt2_s = int(input("Data a ser subtraída(segundos): "))
        dt2 = datetime.timedelta(hours=dt2_h, minutes=dt2_m, seconds=dt2_s)
        print("Segunda data recebida com sucesso.")
    except:
        print("Algo deu errado.")
    else:
        resposta = dt1 - dt2
        print(f"Seu cálculo é de {dt1} - {dt2}\nSua resposta: {resposta}")

elif operacao == "som":
    try:
        dt1_h = int(input("Primeira data (hora): "))
        dt1_m = int(input("Primeira data (minutos): "))
        dt1_s = int(input("Primeira data (segundos): "))
        dt1 = datetime.timedelta(hours=dt1_h, minutes=dt1_m, seconds=dt1_s)
        print("Primeira data recebida com sucesso.")
        dt2_h = int(input("Segunda data (hora): "))
        dt2_m = int(input("Segunda data (minutos): "))
        dt2_s = int(input("Segunda data (segundos): "))
        dt2 = datetime.timedelta(hours=dt2_h, minutes=dt2_m, seconds=dt2_s)
        print("Segunda data recebida com sucesso.")
    except:
        print("Algo deu errado.")
    else:
        resposta = dt1 + dt2
        print(f"Seu cálculo: {dt1} + {dt2}\nSua resposta: {resposta}")
