# This program calculate sales commission
keep_going = 'y'
# Calculating a series of commission
while keep_going == 'y':
    # Get a salesperson's sales and commission rate
    sales = float(input("Enter your sales: "))
    comm_rate = float(input("Enter commission rate: "))
    # Calculate the coomssion (Sales * commission rate)
    commission = sales * comm_rate
    # Display the commission
    print(f"Your commission is {commission:,.2f} ")
    keep_going = input('Do you want to calculate another commission (Enter y for yes):')
