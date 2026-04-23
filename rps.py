def rps(): # Rock, Paper, Scissors
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