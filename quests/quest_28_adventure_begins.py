secret_code = 42
attempts = 3

for i in range(attempts):
    guess = int(input("Enter the secret code: "))

    if guess == secret_code:
        print("Correct! You guessed right.")
        break
    else:
        print("No, Wrong code.")

        if i == attempts - 1:
            print("Too many failed attempts, try again in 2 hours.")
