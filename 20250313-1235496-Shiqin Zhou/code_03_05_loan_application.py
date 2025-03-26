
criteria_annual_salary = 50000
criteria_year_of_work = 5

salary = int(input('Please enter your salary: '))
work_year = int(input('Please enter your work year: '))

if salary >= criteria_annual_salary and work_year > criteria_year_of_work:
    print("Congratulation. You have passed our loan condition.")
else:
    print("Sorry, we have to reject your loan request.")