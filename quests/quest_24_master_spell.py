def ask_for_age():
    age = int(input("Hey there! How old are you? "))
    return age

def can_they_vote(age):
    if age >= 18:
        print("You eligble to vote!")
    else:
        print("You are underage to vote now")

adventurer_age = ask_for_age()
can_they_vote(adventurer_age)
