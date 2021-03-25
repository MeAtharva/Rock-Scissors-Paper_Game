import random

i = 1

while i <= 5:
    
    print("Alert! There are only 5 chances for play the game\n")
    user = input("Enter your choice: R for rock, S for scissors, P for paper: ")
   
    j = 0
    k = 0

    lists = ['R', 'S', 'P']   
    choice = random.choice(lists)

    if (user == choice):
        print("Choice is same, Try Again!\n")
            
    elif ((user == 'R' and choice == 'S') or (user == 'R' and choice == 'P') or (user == 'S' and choice == 'P')):
        print("Computer chose: " + choice)
        print("You chose: " + user)
        print("You Win!\n")
        j += 1

    elif ((user == 'S' and choice == 'R') or (user == 'P' and choice == 'R') or (user == 'P' and choice == 'S')):
        print("Computer chose: " + choice)
        print("You chose: " + user)
        print("You Lose!\n")
        k += 1

    else:
        print('Invalid Choice, Try Again\n')

    print('You used ' + str(i) + ' chances\n')    
    i += 1
    
if (i >= 5):
    if ( j < k ):
        print("User has won most of the time\n")
    elif ( j > k ):
        print("Computer has won most of the time\n")
    else:
        print("Both of have won the same number of time\n")

    print("You have finished your chances")
