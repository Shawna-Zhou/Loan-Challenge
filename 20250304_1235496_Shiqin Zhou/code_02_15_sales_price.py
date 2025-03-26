# A store start 20% discount. Get input of customers' choice as original price, and calculate amount of dicount and discounted price. Display the result with proper message

#Set discount
discount_rate = 0.2
# Get original price of customers' choice
Original_price = int(input("Enter your price of your choice: "))
# Calculate the amount of discount
amount_discount = discount_rate * Original_price
# Calculate the discounted price
discount_price = Original_price - amount_discount
# Dispaly the original price, amount of discount and discounted price with proper message
print(f"The original price that cloth is {Original_price:,.2f} yuan.We do an event of discount. All cloth has discount {discount_rate:0%}. So you save {amount_discount:,.2f} yuan, you only need to pay:{discount_price:,.2f }yuan")