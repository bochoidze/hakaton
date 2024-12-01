user_guess = int(input("Enter a Number from 1-10: "))
while user_guess != 3:
    print("Error or Try Again")
    user_guess = int(input("Enter a Number from 1-10: "))
    if user_guess == 3:
        print("Congrats, You are correct!")