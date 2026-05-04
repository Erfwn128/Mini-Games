def guessRandomNumber(): # Generates a random number and asks the user to guess that number.
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