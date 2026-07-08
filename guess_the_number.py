import random
secret_num=random.randint(0,100)
attempts=0
while True:
    guess=int(input("Guess the secret number! "))
    attempts+=1
    if(guess<secret_num):
        print("Oops! Too low...")
    elif(guess>secret_num):
        print("Oops! Too high...")
    else:
        print(f"Congratulations! You guessed correctly in {attempts} attempts.")
        break