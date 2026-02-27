import random

secret_number=random.randint(1,10)
print(secret_number)
attempts=0

while True:
    users_guess=int(input("guess a number"))
    attempts=attempts+1

    if users_guess > secret_number:
        print("number is too high")
    elif users_guess < secret_number:
        print("number is too low")
    else:
        print("your number you guessed  is correct")
        print("total attempts",attempts)
        break