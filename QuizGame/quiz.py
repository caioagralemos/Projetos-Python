import requests
import random

def api_getter():

    url = 'https://the-trivia-api.com/api/questions'
    response = requests.get(url).json()

    return response

def record(points):
    r = open('QuizGame/record.txt', 'r')
    record = r.read()
    r.close()
    if points > int(record):
        print(f"You have a new record! Your previous record was {record}.")
        r = open('QuizGame/record.txt', 'w')
        r.write(str(points))
        r.close()
    elif points <= int(record):
        print(f"Your all-time record is {record}.")

def game_over(points):
    print(f"You lost! You made {points} points.")
    record(points)

    while True:
        playagain = input("Press 'p' to play again or 'q' to quit: ").lower()
        if playagain == 'p' or playagain == 'q':
            break
    
    if playagain == 'p':
        game(0)
    elif playagain == 'q':
        print("\nThank you for playing!\n")

print("\nPick your first question:")

def game(points):
    myapi = api_getter()
    randnum = random.randrange(1,5)

    print("\n1: " + str(myapi[1]['category']) + ' - ' + myapi[1]['difficulty'])
    print("2: " + str(myapi[2]['category']) + ' - ' + myapi[2]['difficulty'])
    print("3: " + str(myapi[3]['category']) + ' - ' + myapi[3]['difficulty'])

    while True:
        choice = input("\nChoose between 1, 2 and 3: ")
        if choice == '1' or choice == '2' or choice == '3':
            break

    if choice == "1":
        print("\n####################\n")
        print('Your question is: ')
        print(myapi[1]['question'])

        dict = {1: "",2: "",3: "",4: ""}

        if randnum == 1:
            dict[4] = myapi[1]['correctAnswer']
            dict[1] = myapi[1]['incorrectAnswers'][0]
            dict[2] = myapi[1]['incorrectAnswers'][1]
            dict[3] = myapi[1]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])

        elif randnum == 2:
            dict[1] = myapi[1]['correctAnswer']
            dict[2] = myapi[1]['incorrectAnswers'][0]
            dict[4] = myapi[1]['incorrectAnswers'][1]
            dict[3] = myapi[1]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 3:
            dict[3] = myapi[1]['correctAnswer']
            dict[1] = myapi[1]['incorrectAnswers'][0]
            dict[2] = myapi[1]['incorrectAnswers'][1]
            dict[4] = myapi[1]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 4:
            dict[2] = myapi[1]['correctAnswer']
            dict[4] = myapi[1]['incorrectAnswers'][0]
            dict[1] = myapi[1]['incorrectAnswers'][1]
            dict[3] = myapi[1]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])  


        while True:
            answer = input("\nInput your guess: ")

            if answer == "1" or answer == "2" or answer == "3" or answer == "4":
                break

        if dict[int(answer)] == myapi[1]['correctAnswer']:
            print("Right answer!\n\nNext question:")
            if myapi[1]['difficulty'] == 'easy':
                points += 1
            elif myapi[1]['difficulty'] == 'medium':
                points += 2
            elif myapi[1]['difficulty'] == 'hard':
                points += 3
            game(points)
        else:
            print(f"Wrong answer. The answer is {myapi[1]['correctAnswer']}")
            game_over(points)

    elif choice == "2":
        print("\n####################\n")
        print('Your question is: ')
        print(myapi[2]['question'])

        dict = {1: "",2: "",3: "",4: ""}

        if randnum == 1:
            dict[4] = myapi[2]['correctAnswer']
            dict[1] = myapi[2]['incorrectAnswers'][0]
            dict[2] = myapi[2]['incorrectAnswers'][1]
            dict[3] = myapi[2]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])

        elif randnum == 2:
            dict[1] = myapi[2]['correctAnswer']
            dict[2] = myapi[2]['incorrectAnswers'][0]
            dict[4] = myapi[2]['incorrectAnswers'][1]
            dict[3] = myapi[2]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 3:
            dict[3] = myapi[2]['correctAnswer']
            dict[1] = myapi[2]['incorrectAnswers'][0]
            dict[2] = myapi[2]['incorrectAnswers'][1]
            dict[4] = myapi[2]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 4:
            dict[2] = myapi[2]['correctAnswer']
            dict[4] = myapi[2]['incorrectAnswers'][0]
            dict[1] = myapi[2]['incorrectAnswers'][1]
            dict[3] = myapi[2]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])  
        while True:
            answer = input("\nInput your guess: ")

            if answer == "1" or answer == "2" or answer == "3" or answer == "4":
                break

        if dict[int(answer)] == myapi[2]['correctAnswer']:
            print("Right answer!\n\nNext question:")
            if myapi[2]['difficulty'] == 'easy':
                points += 1
            elif myapi[2]['difficulty'] == 'medium':
                points += 2
            elif myapi[2]['difficulty'] == 'hard':
                points += 3
            game(points)
        else:
            print(f"Wrong answer. The answer is {myapi[2]['correctAnswer']}")
            game_over(points)

    elif choice == "3":
        print("\n####################\n")
        print('Your question is: ')
        print(myapi[3]['question'])

        dict = {1: "",2: "",3: "",4: ""}

        if randnum == 1:
            dict[4] = myapi[3]['correctAnswer']
            dict[1] = myapi[3]['incorrectAnswers'][0]
            dict[2] = myapi[3]['incorrectAnswers'][1]
            dict[3] = myapi[3]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])

        elif randnum == 2:
            dict[1] = myapi[3]['correctAnswer']
            dict[2] = myapi[3]['incorrectAnswers'][0]
            dict[4] = myapi[3]['incorrectAnswers'][1]
            dict[3] = myapi[3]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 3:
            dict[3] = myapi[3]['correctAnswer']
            dict[1] = myapi[3]['incorrectAnswers'][0]
            dict[2] = myapi[3]['incorrectAnswers'][1]
            dict[4] = myapi[3]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4]) 

        elif randnum == 4:
            dict[2] = myapi[3]['correctAnswer']
            dict[4] = myapi[3]['incorrectAnswers'][0]
            dict[1] = myapi[3]['incorrectAnswers'][1]
            dict[3] = myapi[3]['incorrectAnswers'][2]

            #random.shuffle(dict)

            print("1: " + dict[1])
            print("2: " + dict[2])
            print("3: " + dict[3])
            print("4: " + dict[4])  

        while True:
            answer = input("\nInput your guess: ")

            if answer == "1" or answer == "2" or answer == "3" or answer == "4":
                break

        if dict[int(answer)] == myapi[3]['correctAnswer']:
            print("Right answer!\n\nNext question:")
            if myapi[3]['difficulty'] == 'easy':
                points += 1
            elif myapi[3]['difficulty'] == 'medium':
                points += 2
            elif myapi[3]['difficulty'] == 'hard':
                points += 3
            game(points)
        else:
            print(f"Wrong answer. The answer is {myapi[3]['correctAnswer']}")
            game_over(points)

game(0)
