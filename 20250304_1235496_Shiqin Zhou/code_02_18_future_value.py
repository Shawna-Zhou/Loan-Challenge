# Calculating values
# Future value
# Present value
# Interest_rate
# Year

#calculate how much money you have to seposit today to get a desired money in the future. Get relevant information form user. (interest_rate, year)
# Get the desired future value
future_value = int(input("Please enter what is your desired money in the future: "))
# Get the annual interest rate
interest_rate = float(input("What is the interest_rate: "))
# Get the year money will stay
years = int(input("Please tell me how many years you will deposit: "))
# Calculate the amount needed to deposit
present_value = future_value/(1 + interest_rate)**years
# Display the values that you need to calculate present value with proper message
print(f"So you will need to deposit {present_value:,.2f} yuan today, then you can get {future_value:,.2f} in {years} years.")
# The number suppose to be formatted properly
