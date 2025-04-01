# Get starting number and end number from user

start = int(input("Please tell me which number you want to start at: "))
end = int(input("Please tell me which number you want to end with: "))
print("    Number\tSquare")
print("-----------------------------")
# Print sequencial number 1 to 10
for num in range(start, end+1):
    square = num ** 2
    print(num, "\t", square)



