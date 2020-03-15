import random

print "********************************************************"
print "Welcome to Rock Paper Scissors..."
print "The rules are simple:"
print "The computer and user choose from Rock, Paper, or Scissors."
print "Rock crushes scissors."
print "Paper covers rock."
print "and"
print "Scissors cut paper."
print "You will play the computer...the first to reach 3 wins wins the match."
print "Good luck!"
print "************************************************************"""

user_win = 0
computer_win= 0

user_name= raw_input("Whats Your Name? ")

while True:

    computer_choice = ""

    user_choice = raw_input("Please choose (R) Rock, (P) Paper, or (S) Scissors: ").upper()

    random_number = random.randint(1,3)

    if random_number == 1:
        computer_choice = "R"

    if random_number == 2:
        computer_choice = "P"

    if random_number == 3:
        computer_choice = "S"


    if computer_choice == "R":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        The computer chose rock.""")

    elif computer_choice == "P":
        print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    The computer chose paper.""")


    elif computer_choice == "S":
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        The computer chose scissors.""")

    print ""

    if (computer_choice == "R" and user_choice == "P") or \
            (computer_choice == "P" and user_choice == "S") or \
                            computer_choice == "S" and user_choice == "R":
        print "You win!"
        user_win +=1
        print user_name, user_win
        print "computer=", computer_win
    elif (computer_choice == "R" and user_choice == "S") or \
            (computer_choice == "P" and user_choice == "R") or \
            (computer_choice == "S" and user_choice == "P"):
        print "You lose!"
        computer_win +=1
        print user_name, user_win
        print "computer=", computer_win

    else:
        print "Ties"
        print user_name, user_win
        print "computer=", computer_win

    if computer_win == 3:
        print  user_name,"LOST"
        user_win =0
        computer_win = 0

        delay = raw_input("You want to play another game Y/N ? ")
        if delay == "y":
            continue
        else:
            break

    elif user_win == 3:
        print user_name,"WON"
        user_win = 0
        computer_win = 0

        delay = raw_input("You want to play another game Y/N ? ")

        if delay == "y":
            continue
        else:
            break


