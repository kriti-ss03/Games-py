# "const" 
# 'cmmt "+" includes apostr' 
# '''multiple lines'''
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

game_img=[rock,paper,scissors]

user=int(input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors"))
if(user>=0 and user<=2):
  print(game_img[user])

computer=random.randint(0,2)
print("computer chose")
print(game_img[computer])

if(user>=3 or user<0):
  print("You typed an invalid number")
elif(user==0 and computer==2):
  print("You win")
elif(computer==0 and user==2):
  print("You lose")
elif computer>user:
  print("You lose")
else:
 print("You won")