def creatPassword(sala): # ساختن پسورد تصادفی توسط ربات
    import string, random

    while True:
        lenght = int(input("Enter the password lenght: "))
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-+_?><:;"    
        password = ''.join([random.choice(chars) for i in range(lenght)])

        print(f"Your the password is: {password}")

        while True:
            answer = input("Do you want creat password again? (Y/n): ").lower()
            if answer == 'n' or answer == 'y':
                break
        if answer == 'n':
            break
#---------------------------------------------------
def guessRandomNumber(): # ایجاد یک عدد تصادفی و حدس آن عدد توسط کاربر
    import random

    # Create list for round number and  return best round guess
    best_guess = []

    def welcome():
        print("Ooh.. welcome to the funny Game!")
        print()

    def finished(random_number, counter):
        print(f"\nGood Game! The computer number is {random_number} and you won in round {counter}")
        best_guess.append(counter)
        print(best_guess)
        min_guess = best_guess[0]

        for i in best_guess:
            if min_guess > i:
                min_guess = i
        print(f"The best and top round guess is {min_guess} round!")

        while True:
            again_answer = input("Do you want to play again(Y/N): ").upper()
            if again_answer == "Y" or again_answer == "N":
                break
        return again_answer == "Y"
    def win(random_number, guess):
        return random_number == guess

    def get_guess():
        my_guess = int(input("Enter the number beetwin 1 - 20: "))
        return my_guess

    def answer(random, user):
        if user > random:
            return f"{user} > randomNumber"
        elif user < random:
            return f"{user} < randomNumber"
        return f"Woow..! You won, Gooood guess!"

    welcome()
    again_playing = True

    while(again_playing):
        # Create the random number in computer between 1 and 20
        random_number = random.randint(1, 20)

        # The first guess is 0
        guess = 0

        # In which round did the user guess the random number
        counter = 0

        while (not win(random_number, guess)):
            guess = get_guess()
            counter += 1
            print(answer(random_number, guess))

        again_playing = finished(random_number, counter)
#---------------------------------------------------
def rps(): # بازی سنگ، کاغذ، قیچی
    import random

    around = 1
    client_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]

    while (client_score < 3) and (computer_score < 3):
        print(f"Round {around}")
        computer = random.choice(choices)

        while True:
            client_index = int(input("Choose (1-rock, 2-paper, 3-scissors): ")) - 1
            if client_index in [0, 1, 2]:
                break
            else:
                print("Please select within the specified range.")
    
        client = choices[client_index]
        print(f"Client chose: {client}")
        print(f"Computer chose: {computer}")

        if client == computer:
            print("• It's a tie!")
        elif client == "paper" and computer == "rock":
            print("• You win!")
            client_score += 1
        elif client == "rock" and computer == "scissors":
            print("• You win!")
            client_score += 1
        elif client == "scissors" and computer == "paper":
            print("• You win!")
            client_score += 1
        else:
            print("• Computer win!")
            computer_score += 1

        print(f"Score: client: {client_score}, computer: {computer_score}")
        around += 1
        print("-" * 10)

    if client_score > computer_score:
        print("The ultimate winner of this mini-game is the {user}.")
    elif client_score < computer_score:
        print("The ultimate winner of this mini-game is the {computer}.")
#---------------------------------------------------
def betting(): # شرط بندی اگر تاس زوج باشه یا فرد
    import random

    user_coin = 100
    around = 1
    won = 0
    lost = 0

    while user_coin > 0:
        dice = random.randint(1, 6)
        while True:
            coin_bet = int(input("Please enter the bet amount: "))
            if (coin_bet <= user_coin) and (coin_bet >= 1):
                break
            else:
                print(f"Enter the bet amount between 1 and {user_coin}")

        while True:
            choice = input("Choose whether the dice is (even/odd): ").lower()
            if choice in ["even", "odd"]:
                break
            else:
                print("⛔ Don't use meaningless words!")

        if ((choice == "even") and (dice % 2 == 0)) or ((choice == "odd") and (dice % 2 != 0)):
            user_coin += coin_bet
            won += 1
            print("=" * 15)
            print(
                f"🪙  Your coins: {user_coin - coin_bet}\n"
                f"🎲 Choose (even/odd): {choice}\n"
                f"🎲 Dice rolled: {dice}\n"
                f"✅ You won! +{coin_bet} coins\n"
                f"💰 Your coins now: {user_coin}"
            )
            print("=" * 15)
        else:
            user_coin -= coin_bet
            lost += 1
            print("=" * 15)
            print(
                f"🪙  Your coins: 100\n"
                f"🎲 Choose (even/odd): {choice}\n"
                f"🎲 Dice rolled: {dice}\n"
                f"❌ You lost! -{coin_bet} coins\n"
                f"💰 Your coins now: {user_coin}"
            )
            print("=" * 15)

        around += 1
        while True:
            exit_btn = input("❓ Do you want to exit the game? (y/n): ").lower()
            if exit_btn in ["y", "n"]:
                break
            else:
                print("⚠️  Just answer with y and n!")
        if exit_btn == "y":
            break

    print("*" * 20)
    print(
        f"🎮 Game Over!\n"
        f"💰 Final coins: {user_coin}\n"
        f"📈 You played {around} rounds\n"
        f"🏆 You won {won} rounds and lost {lost} rounds\n"
        "👋 Goodbye!"
    )
    