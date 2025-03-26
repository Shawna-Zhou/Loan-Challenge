# This programming determine whether you will accept loan application or reject based on annual salary and year of work. annual salary >= 50000 and work year > 5. You have tell them how much salary or year of work need more
criteria_annual_salary = 50000
criteria_year_of_work = 5

salary = int(input('Please enter your salary: '))
work_year = int(input('Please enter your work year: '))

if salary >= criteria_annual_salary:
    if work_year >= criteria_year_of_work:
       print("Congratulation. You have passed our loan condition.")
    else:
        need_year = criteria_year_of_work - work_year
        print(f"Sorry, we have to reject your loan request. You still need to work {need_year}")
else:
    if work_year >= criteria_year_of_work:
       need_salary = criteria_annual_salary - salary
       print(f"Sorry. You have to earn extra {need_salary:,.2f}yuan.")
    else:
        need_salary = criteria_annual_salary - salary
        need_year = criteria_year_of_work - work_year
        print(f"Sorry, we have to reject your loan request. You still need to work {need_year}. Also you need to earn extra {need_salary:,.2f}")



