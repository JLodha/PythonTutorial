secret_word = "JhX"
guess = ""
count = 0
count_limit = 5
out_of_count = False

while guess != secret_word and not(out_of_count):
    if count<count_limit :
        guess = input("Enter your guess: ")
        count+= 1
        if guess!=secret_word:
            print("Incorrect guess!")
    else:
        out_of_count = True

if out_of_count :
    print("Sorry but you have lost the game!")
else:
    print("You won the game in " + str(count) + " tries.")


