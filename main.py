from random import randint as r
randNo = r(1, 100)

a = True

guess = 0

while(a == True):

    num = int(input("Enter your guess : "))
    
    guess += 1

    if randNo == num:
        print("Congratulations! you've guessed it right...")
        print(f"Your score : {guess}")
        a = False

    else:

        if num < randNo:
            print("Wrong guess. Enter a greater number.")
            a = True

        else:
            print("Wrong guess. Enter a smaller number.")
            a = True

with open("HiScore.txt", "w+") as f:
    file = f.read()
    if file == "" or int(file) > guess:
        f.write(str(guess))
