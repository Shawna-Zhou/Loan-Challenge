# In this script, we will practice print function
print('Shawna Zhou')  #single quotation practice
print("It's reallt nice a day")  #double quotation practice
print("""For the triple quotation, Chad said,"It's important to understand how to use this function" """)  #triple quotation practice

# Variable Practice
room = "Banyan 215"
print("I am staying in room number")
print(room) 

name = "Shawna"
age = "20"
building = "Banyan"
school = "WKU"
print("Hello, my name is",name,"Nice to meet you.","I am",age,"years old.","What is about you?","I live in",building,"I heard that you go to school. What was that?",school,"?")

# Convert program line 11 to 15 using f string
print(f"Hello,my name is {name},Nice to meet you. I am {age} years old. What's about you? I live in {building}, I heard that you go to school. What was that? {school}?")

# Print the same message by information that you get from key user keybaord input
name = input("Please enter your name: ")
age = input("Please enter your age: ")
bulding = input("Please enter your building: ")
school = input("Please enter your school: ")
print(f"Hello,my name is {name},Nice to meet you. I am {age} years old. What's about you? I live in {building}, I heard that you go to school. What was that? {school}?")