
winning_number = 57
guess = 1
number = int(input("Guess a number between 1 and 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You Win! : you guess this number in {guess} time")
        guess += 1
        game_over = True
    else:
        if number < winning_number:
            print("Too low")
            guess += 1
            number = int(input("Guess again : "))
        else:
            print("Too high")
            guess += 1
            number = int(input("Guess again : "))        

