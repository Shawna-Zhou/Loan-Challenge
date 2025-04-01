# Get starting and ending num. If start is grater than end, make it reduce number

start = int(input("Please tell me which number you want to start at: "))
end = int(input("Please tell me which number you want to end with: "))
if start > end :
    print("    Number\tSquare")
    print("-----------------------------")
    for num in range(start, end-1, -1):
        square = num ** 2
        print(num, "\t", square)
        
else:
    print("Number\tSquare")
    print("----------------------------")
    for num in range(start, end + 1):
        square = num ** 2
        print(num, "\t", square)

    