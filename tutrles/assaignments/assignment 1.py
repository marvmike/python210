import random

### if statement
## check if a number is even

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")

##Display a message if a list is empty.
my_list = []

if len(my_list) == 0:
    print("The list is empty")

##Write a script to check if a number as odd or even.
number = int(input("Enter another number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

##Write a script for Temp categories.
temp = float(input("Enter the temperature: "))

if temp < 0:
    print("It's freezing cold")
elif temp < 10:
    print("It's cold")
elif temp < 20:
    print("It's moderate")
elif temp < 25:
    print("It's warm")
elif temp > 35:
    print("It's hot")
else:
    print("The temperature is in a comfortable range")


### for loop
##Print each character in a string.
my_string = "Hello, World!"

for char in my_string:
    print(char)


##Create a list of squares of the first 10 natural numbers.
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)


###while loop
##Add numbers until sum reaches 100.
sum = 0
number = 1

while sum < 100:
    sum += number
    number += 1

print(f"The sum is {sum}")

##Guessing game with break on correct guess.
random_number = random.randint(1, 10)
attempts = 4

for _ in range(attempts):
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < random_number:
        print("Guess higher!")
    else:
        print("Guess lower!")

print(f"The random number was: {random_number}")


