# This script will get input as large numver of seconds, then calculate the hours, minutes, and seconds. 5//2   5%2

print(5 // 2)
print(5 % 2)

# Get a numbers of seconds
num_sec = int(input("Please enter your seconds: "))
# Calculate the hours
hours = num_sec // 3600
# Calculate the minute
minute = (num_sec // 60) 
# Calculate the remained seconds
remained_sec = num_sec % 60
# Dispaly hours, minute and seconds with proper message
print(f"According to your number of seconds, it is {hours} h, or it is {minute} min. And  it remain {remained_sec} s.")