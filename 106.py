from random import randint

number = randint(0, 10)
chance = 5

print("Welcome To Number Guessing Game")
while chance > 0:
    print(f"You have {chance} chances left")
    guess = input("Guess the number : ")
    try:
        guess = int(guess)
        if guess == number:
            print("You won!")
            break
        elif guess > number:
            print("Try smaller than", guess)
        elif guess < number:
            print("Try bigger than", guess)

        print()
        chance -= 1
    except ValueError:
        print("Invalid Input Try Again")

if chance == 0:
    print("You lost! The number was", number)

