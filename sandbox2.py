answer = 7 
print("I'm thinking of a number betwee  1 to 10, Can you guess what it is?")
guess = input("enter your guess: ")

try:
    guess = int(guess)
except:
    print("That's not a valid integer, Please try again.")
    exit()

if guess == answer:
        print("congratulations! You guessed the correct number.")
elif guess < answer:
     print("Too Low! Try again.")
elif guess > answer:
    print("Too high! Try again.")
    
