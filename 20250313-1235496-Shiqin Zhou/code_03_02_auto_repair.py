# This program will calculate payment in normal case, you will get 1000yuan per hour. Legal work per week is 40 hour. Your contract said if you work more than legal work hour, you will get different pay ratio, overtime pay ratio. You will program that get input from worker and calculate the total payment considering normal hour or overtime work hour
Base_hour = 40
Hourly_payment = 1000
OT_Payratio = 1.5


work_hour = int(input("Please enter your working hour this week: "))
if work_hour <= 40:
    total_payment = work_hour * Hourly_payment
    print(f"So this week you will get {total_payment:,.2f}yuan.")

else:
    extraworkinghour = work_hour - Base_hour
    overtimepayment = extraworkinghour * Hourly_payment * OT_Payratio
    total_payment = Base_hour * Hourly_payment + overtimepayment
    print(f"So this week, your total salary is {total_payment:,.2f}yuan, including overtime payment {overtimepayment:,.2f}yuan with overtime ratio {OT_Payratio:.2%}")

