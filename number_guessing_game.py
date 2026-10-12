import random
print("Welcome to The Price Is Right !")
number = random.randint(1, 100)
attempts = 0

while True:
    attempts = attempts + 1
    response = int(input("Please enter a number : "))
    if response > number : 
        print("The number is lower!")
    elif response < number :
        print("The number is higher!")
    elif response == number:
        print(f"Good job ! The response is {number}")
        break

print(f"You guessed it in {attempts} attempts!")
