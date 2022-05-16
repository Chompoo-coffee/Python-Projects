''' Unfinished project '''

user_guess = input()
computer_guess = range(100)
win = "Congratulations!\nYou win!!!"

def more_and_guess():
    answer = input()
    if answer == "more":
        print("So what's your number guess?")
        number_guess = input()
        if  number_guess == computer_guess:
            print(win)
        if number_guess > 75 and number_guess < 83 and number_guess < 100:
            print("Let's try another\nIs the number is more or less than 83?")
            more_and_guess()
        if number_guess > 83 and number_guess < 100:
            more_and_guess()

print(user_guess)
print(computer_guess)

if user_guess == computer_guess:
    print(win)
else:
    print("Let's try another\nIs the number is more or less than 50?" )
    more_and_guess()
