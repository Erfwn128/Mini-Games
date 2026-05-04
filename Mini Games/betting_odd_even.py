def betting(): # Betting on the odd or even number of dice
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
    