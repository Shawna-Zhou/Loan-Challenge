import streamlit as st
st.title("Happy Loan")

# Criteria 
criteria_annual_salary = 50000
criteria_year_of_work = 5

# Initialize the state variable
if 'passed' not in st.session_state:
    st.session_state.passed = False

# Step 1: Qualification Check
if not st.session_state.passed:
    st.subheader("Step 1: Qualification Check")
    salary = st.number_input('Please enter your salary: ')
    work_year = st.number_input('Please enter your work year: ')
    if st.button('Submit'):
      if salary >= criteria_annual_salary and work_year >= criteria_year_of_work:
        st.success("Congratulation. You have passed our loan condition.")
        st.session_state.passed = True
      else:
        st.error("Sorry, we have to reject your loan request.")

# Step 2: Loan Calculator
# session_state is like a storing dictionary
if st.session_state.passed:
   st.subheader("Step 2: Loan Payment Calcultor")

   # User Enter
   loan_amount = st.number_input("Please enter how much you want: ")
   annual_rate = st.number_input("Please enter annual interest rate(%): ")
   year = st.number_input("Please enter how long you want yo borrow: ")

   if st.button('Calculate'):
      monthly_rate = annual_rate / 100 / 12
      months = int(year * 12)
      monthly_payment = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

      total_payment = monthly_payment * months
      total_interest = total_payment - loan_amount

      st.success(f'Monthly Payment is {monthly_payment:,.2f} yuan. ')
      st.info(f'Total Payment is {total_payment:,.2f} yuan | Interest is {total_interest:,.2f} yuan')
      years_part = months // 12
      months_part = months % 12
      st.write(f"Repayment Period is {years_part} year(s) and {months_part} month(s)")


