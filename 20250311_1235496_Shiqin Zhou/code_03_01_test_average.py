# You have yo write a python program that get three score and calculate average score. Set high_score as 95, then compare to the high_score, if the users average score is higher than high_score, show congratulation message with current score, otherwise dispaly average_score

# Set high score
high_score = 95
# Get score 1
score_1 = float(input("Please enter score of Math : "))
# Get score 2
score_2 = float(input("Please enter score of English : "))
# Get score 3
score_3 = float(input("Please enter score of Chinese : "))
# Calculate the average score
average_score = float((score_1 + score_2 + score_3) / 3)
# Determine whether ther average score is higher than high_score. If the average score is greater than high_score
   #Display high score and user's average score with congratulation message
if average_score >= high_score:
    print(f"Congratulation! Your average score of 3 subjects is very good, it is {average_score:.2f}, higher than {high_score:.2f}")
# Otherwise
else:
   # Dispaly current average score
   print(f"Your average score is {average_score:.2f}. ")