import random
n = random.randint(1, 101)
cout = 12
guess = int(input("Enter an integer from 1 to 100: "))
while n != "guess" and cout != 5:
    cout -= 2
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print("you guessed it!")
        print("Score:" + str(cout))
        break
    if cout == 5:
        print("You loss!!")
