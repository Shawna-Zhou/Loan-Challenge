# This program will calculate running total of num as much as the user enter

start = int(input("enter starting num: "))
end = int(input("Enter the end num: "))

total = 0.0
#loop
for num in range(start, end +1):

    total += num

print(f" All number added up from{start} to {end} is {total}")