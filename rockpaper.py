import random
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

#Write your code below this line 👇
choice = [rock,paper,scissors]

user = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))
new = choice[user]
computer = random.randint(0,2)
new2 = choice[computer]
if user == computer:
  print("you choose\n",new , "computer choose:\n",new2,"Match Draw..!")
elif user == 0 and computer == 1:
  print("you choose:",new, "computer choose:", new2,"you wins..!")
elif user == 1 and computer == 2:
  print("you choose:", new, "computer choose:",new2,"you loose..!" )
elif user == 2 and computer == 1:
  print("you choose", new , "computer choose:", new2,"you wins..!")
elif user == 2 and computer == 0:
  print("you choose:", new, "computer choose:",new2,"you lose..!")
elif user == 1 and computer == 0:
  print("you choose:", new, "computer choose:",new2, "you wins...!")
elif user > computer:
  print("you choose:",new, "computer choose:",new2,"you wins..!")

else:
  print('exit')

 
