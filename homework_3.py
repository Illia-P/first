# Магическое число.
import random

random_number = random.randint(1, 100)

x = int()
attempts = 0
while x != random_number:
    x = int(input("Enter a number: "))

    if random_number > x:
        print("More")
        attempts += 1
    elif random_number == x:
        print("Bingo, ", "attempts :",attempts )
    else:
        print("less")
        attempts += 1


# Алгоритм Эвклида. НОД - наибольший общий делитель
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)