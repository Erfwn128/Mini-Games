def creatPassword(sala): # Generate a random password
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