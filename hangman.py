def hangman(): # Guess the computer's chosen word
    import random

    score = 0
    around = 1
    letter_list = []
    animals = ["tiger", "rabbit", "dolphin", "penguin", "giraffe", "cheetah", "kangaroo", "octopus", "crocodile", "butterfly"]
    animal_cpu = random.choice(animals)
    chance = len(animal_cpu)

    print(animal_cpu)
    print("⚡ Welcome to the word guessing game!")
    print("👾 Guess the word chosen by the computer.")
    word_hide = ["_"] * len(animal_cpu)

    while chance > 0:
        print(f"💠 Score: {score}")
        print(f"🕸️  Chance: {chance}")
        print(f"Word: {' '.join(word_hide)}")

        while True:
            print(f" round {around} ".center(25, "="))
            letter = input("Guess the letter: ")
            if (len(letter) == 1) and (letter.isalpha()) and (letter.isascii()):
                break
            else:
                print("⚠️  Please enter the one letter!")
                continue

        if letter in letter_list:
            print("⚠️  You already guessed that letter! Try another one.")
            continue

        letter_list.append(letter)

        i = 0
        found = False
        for item in animal_cpu:
            if letter == item:
                word_hide[i] = letter
                score += 10
                found = True
            i += 1
        if found:
            print("🟢 Goood guess!")
        else:
            print(f"🔴 The word you selected did not exist.")
            chance -= 1
            score -= 5

        if ''.join(word_hide) == animal_cpu:
            print(f"✅ You managed to find the word in round {around}")
            print(f"Your's score is: {score}")
            print(f"The word was: {animal_cpu}")
            break

        around += 1

    if chance == 0:
        print("❌ Your chance is lost.")
        print(f"The word was: {animal_cpu}")
