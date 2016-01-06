import random 
secret_number = random.randint(1,100)
print secret_number
number_of_guesses = []


name = raw_input("Hey, What's Your Name?")
prompt = name + " Guess a number between 1 and 100!"

while True:
    user_choice = int(raw_input("Wanna play game? 1= Yes 2 = No"))
    if user_choice == 1:
        while prompt != secret_number:
            while True:
                try:
                    user_guess = int(raw_input(prompt))
                    break
                except ValueError:
                    print "THAT WAS OBVIOUSLY NOT A NUMBER... Try typing a number you git."

            number_of_guesses.append(user_guess)
            if user_guess >= 101:
                print "YOU'RE A LOSER! THAT'S OUT OF RANGE! GUESS AGAIN GIT!"
            elif user_guess <=0:
                print "YOU'RE A LOSER! THAT'S OUT OF RANGE! GUESS AGAIN GIT!"
            elif user_guess < secret_number:
                print "That is too low, try again"
            elif user_guess > secret_number:
                print "That is too high, try again" 
            else:
                print "Winner Winner Chicken Dinner!"
                print "It took you {n} guesses!".format(n =len(number_of_guesses))
        
    else:
        print "K bye."
        break

            
    



