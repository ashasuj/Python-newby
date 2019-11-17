secret_number = 9

guess_counter =0
guess_limit =3
while guess_counter <guess_limit:
    guess = input("Secret Number: ")
    if int(guess) == 9:
        print("You have won!!")
    else :
        guess_counter = guess_counter+1
print("You have exhausted your attempts") 	