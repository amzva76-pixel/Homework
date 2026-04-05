import random
playing = True
number = str(random.randint(1, 10))

print(" I will generate a number from 1 to 10 and you have to guess it on time.")
print(" The game ends When you get 1 hero.")

while playing:
    guess = input(" Guess the number: \n")
    if guess == number:
        print(" You got it right! You are a hero!")
        print(" The number was " , number)

        break
    else:
        print(" Wrong guess! Try again.")