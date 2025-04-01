# You will write a program that help scientist. There is a system that you can control thermostat and see the tempreture of substamce. The system suppose to less tempreture then maximum temprature is 100
# Your python program will help scientist asking current temprature and if current temprature of substance is higher than maxium temprature, show instruction and ask temprature until the temprature is below maximum temprature

# Set the maximum temprature
max_temp = 100
keep_going = 'temprature'
# Asking current temprature
temprature = float(input("Please enter the current tempature: "))
# While the temprature is higher to the maximum temprature
while temprature >= max_temp:
    # Display instruction
    # Display a message that " the temprature is too high.
    print(" The current temprature is too high. Please turn down and wait 5 minutes.") 
    # Turn the thermostat down and wait 5 min. Then take the temprature again and enter it"
    temprature = float(input("What is your current temprature right now: "))
    # Update temprature
# Otherwise
print("All temprature is fine")

    # Display " temprature is fine"