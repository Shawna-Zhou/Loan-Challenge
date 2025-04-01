# This program will calculate running total of num as much as the user enter

howmany = int(input(" Enter how many number that you add up: "))

total = 0.0
#loop
for num in range(howmany):
    number = int(input("Put a number to add up: "))
    total += number

print(f" the total is {total}")