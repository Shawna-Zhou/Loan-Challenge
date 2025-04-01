import streamlit as st
# Make this streamlit app

start = int(st.number_input("Please tell me which number you want to start at: "))
end = int(st.number_input("Please tell me which number you want to end with: "))
if st.button("Submit"):
    st.write("    Number\tSquare")
    st.write("-----------------------------")
    for num in range(start, end+1):
        square = num ** 2
        st.write(num, "\t", square)