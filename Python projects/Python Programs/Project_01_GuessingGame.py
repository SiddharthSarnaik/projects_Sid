import random
import time
number = random.randint(1, 10)
guess = int (input("Enter your guess (1-10): "))
guess_count = 1

while guess != number:
    time.sleep(1)  # Add a small delay for better user experience
    print("thinking....")
    time.sleep(2)
    if number > guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Enter your guess (1-10): "))
    guess_count += 1
    

print("Congratulations! You guessed the number which is : ", number, ", it took you", guess_count, "tries.")
        