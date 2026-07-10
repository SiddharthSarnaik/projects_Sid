import random
import time
number = random.randint(1, 10)
name = input("Enter your name: ")
time.sleep(1)
print("Hmmm....")
time.sleep(1)
print("Hello", name, "Welcome to the guessing game!")
time.sleep(1)  # Add a small delay for better user experience
guess = int (input("Enter a number between 1 and 10 to guess a correct number: "))
guess_count = 1

while guess != number:
    guess_count += 1
    time.sleep(1)  # Add a small delay for better user experience
    print("thinking....")
    time.sleep(2)  # Add a small delay for better user experience
    if guess > number:
        guess = int(input(" wrong. your guess is too high. Enter your guess (1-10): "))
    else:
        guess = int(input(" wrong. your guess is too low. Enter your guess (1-10): "))

print("Congratulations! You guessed the number which is : ", number, ", it took you", guess_count, "tries.")
        