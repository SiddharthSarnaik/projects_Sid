import random
import time
number = random.randint(1, 10)
guess = int (input("Enter your guess (1-10): "))
guess_count = 1

while guess != number:
    guess_count += 1
    time.sleep(1)  # Add a small delay for better user experience
    print("thinking....")
    time.sleep(2)
    if guess > number:
        guess = int(input(" wrong. your guess is too high. Enter your guess (1-10): "))
    else:
        guess = int(input(" wrong. your guess is too low. Enter your guess (1-10): "))
    
    
    

print("Congratulations! You guessed the number which is : ", number, ", it took you", guess_count, "tries.")
        