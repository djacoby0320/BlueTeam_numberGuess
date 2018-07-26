import random
num = random.randint(1,9)

counter = 0
guess = 0

print ("Hello! Please guess a number between 1 and 9!")
print ("If you don't want to play, type 'exit'")


while guess != num and guess != "exit":
    try:
      guess = input ("Guess a number")
      if guess == "exit":
        break

      guess = int(guess)
      counter += 1

      if guess < num and guess >= 1:
        print ("Pick a higher number!")
      elif guess > num and guess <= 9:
        print ("Pick a lower number!")
      elif guess < 1 or guess > 9:
        print ("Please select a number between 1 and 9")
      else:
        print ("Correct!")
    except:
        print("Please enter a valid number between 1 and 9.")

if guess == num:
    print ("It took you" ,counter, "tries to pick the number.")
else:
    print("You didn't guess the number! Please try again!")