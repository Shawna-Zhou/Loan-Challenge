# Your have to write a program to calculate total commision for salesman. They got 20% of their commision per product until they sale to 5000. If the salesman make more than 5000, they got 50% of the commision for extra sales. Price for one unit of product is 600 yuan.
sales = int(input('Please tell me how many product you have sold: '))
total_sales = sales * 600
if total_sales <= 5000:
    commission = total_sales * 0.2
    print(f"By selling {sales} products, you can get commission {commission:,.2f}yuan. ")
else:
    
    extra_sales = total_sales - 5000
    commission = 5000 * 0.2 + extra_sales *0.5
    print(f"This month, you can get commission {commission:,.2f}yuan, with extra sales {extra_sales:,.2f}yuan")