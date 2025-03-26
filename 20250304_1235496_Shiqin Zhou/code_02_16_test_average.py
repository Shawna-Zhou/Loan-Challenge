# You will get three exam score and calculate average of the three exam. Dispaly the average exam score with proper message
First_score = int(input("Please enter your First score: "))
Second_score = int(input("Please enter your Second score: "))
Third_score = int(input("Please enter your Third score: "))
average_score = (First_score + Second_score + Third_score) /3
print(f"Your average score is {average_score:,.2f}")