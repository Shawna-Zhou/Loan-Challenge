sales = float(input(" What is your sales total? "))
if sales > 60000:
    bonus = 500
    commission_rate = 0.12
    print(f' Congratuation, you have extra{bonus:,.2f} yuan, and your commission rate has upgraded to {commission_rate:0%} ')
else:
    print(" Sorry, no bonus ")