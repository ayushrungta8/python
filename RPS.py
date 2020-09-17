import random
print("...rock...\n...paper...\n...scissor...\n")

cwin = 0
pwin = 0
for choice in range(0, 5):
    user1 = input("Enter Player 1's choice(Press q to quit):")
    if user1 == 'q':
        break
    user2 = random.randint(1, 3)
    if(user2 == 1):
        user2 = 'rock'
    elif(user2 == 2):
        user2 = 'paper'
    else:
        user2 = 'scissor'
    print(f"Computer's choice:{user2}")

    if(user1 == user2):
        print("Tie\n")
    elif(user1 == 'rock' and user2 == 'paper') or (user1 == 'paper' and user2 == 'scissor') or (user1 == 'scissor' and user2 == 'rock'):
        print("Computer Wins\n")
        cwin += 1
    else:
        print("Player Wins\n")
        pwin += 1
    choice += 1
print(f"Computer's Score:{cwin}\n")
print(f"Player's Score:{pwin}\n")
if pwin > cwin:
    print("Player Wins")
elif cwin > pwin:
    print("Computer Wins")
else:
    print("It's a Tie")
