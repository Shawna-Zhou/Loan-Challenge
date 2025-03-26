# You have to write a code for password login. You set a passsword, and get a password form user. If the password is matched, display greeting message, otherwise, display bye bye message
password = "Shawna"
password_input = input("Please enter your password: ")
if password_input == password:
    print("Welcome Shawna. You are awesome. ")
else:
    print("Sorry, wrong password. Try again.")
