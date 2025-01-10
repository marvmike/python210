# List of my favorite cars
'''cars = [
    "Tesla",
    "Porsche",
    "BMW",
    "Audi",
    "Hell cat"
]
my_fav_cars = [
    "Tesla",
    "BMW",
    "Hell cat"
]

print("My favorite cars:", my_fav_cars)


###exercise 2
my_fav_actors = [
    "Ryan Gosling",
    "Timothee Chalamet",
    "Tom Cruise",
    "Leonardo DiCaprio"
]

print("My favorite actors are:", my_fav_actors)'''

####exercise 3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]

print("Prime numbers in the range:", prime_numbers)

####exercise 4
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')