secret_number = 9
guess = int(input("Guess the secret number: "))

while guess != secret_number:
    print("Wrong!")
    guess = int(input("Try again: "))

print("You got it! The secret number was 9")
