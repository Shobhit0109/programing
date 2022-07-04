from random import randint

magic = randint(0,100)
guess = int(input("\n\tGuess thee magic number: "))

if (guess == magic) :
    print(f"\n\tCorrect guess {guess} is the magic number")

elif guess > magic:
    print("\n\tGuess is higher than magic number")

else:
    print("\n\tGuess is lower than magic number")