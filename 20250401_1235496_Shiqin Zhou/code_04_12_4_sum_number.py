# In this program, you have to use ypur square code and at the end add total of the square
# Make it both starting number is grater than end number or not

total = 0.0

start = int(input("Please tell me which number you want to start at: "))
end = int(input("Please tell me which number you want to end with: "))
print("    Number\tSquare")
print("-----------------------------")

if start > end :
    
    for num in range(start, end-1, -1):
        square = num ** 2
        total += square
        print(num, "\t", square)
        
else:
    print("Number\tSquare")
    print("----------------------------")
    for num in range(start, end + 1):
        square = num ** 2
        total += square
        print(num, "\t", square)

print("------------------------")
print(f"The total of all the squares is {total}")
