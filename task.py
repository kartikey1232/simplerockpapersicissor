rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer=random.randint(0,2)
if player == 0:
    print(rock)
    print("Computer Chose:")
    if computer == 0:
        print(rock)
        print("It's a draw")
    elif computer == 1:
        print(paper)
        print("You Lost")
    else:
        print(scissors)
        print("You Won")
elif player == 1:
    print(paper)
    print("Computer Chose:")
    if computer == 0:
        print(rock)
        print("You Won")
    elif computer == 1:
        print(paper)
        print("It's a Draw")
    else:
        print(scissors)
        print("You Lost")
else:
    print(scissors)
    print("Computer Chose:")
    if computer == 0:
        print(rock)
        print("You Lost")
    elif computer == 1:
        print(paper)
        print("You Won")
    else:
        print(scissors)
        print("It's a draw")