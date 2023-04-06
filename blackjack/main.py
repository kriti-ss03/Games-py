import random
from replit import clear
from art import logo


deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def pick(arr,num,ace):
  sum=0
  while(num>0):
    card=random.randint(0,11)
    arr.append(deck[card])
    if(deck[card]==11):
      ace.append(1)
    sum+=deck[card]
    num-=1
  
  return sum


def play():
  user=[]
  comp=[]
  
  su=0
  sc=0
  # for ace
  fu=[]
  fc=[] 
  
 
  
  su=pick(user,2,fu)
  print(f"Your Cards are {user} and current score is {su}")

  
  sc=pick(comp,2,fc)
  print(f"Computer's Cards are {comp[0]} and X.")
  
  
  to_continue=True
  
  while to_continue:  
    if(su==21 and sc==21):
      to_continue=False
      print(f"Computer's cards are {comp[0]} and {comp[1]}")
      print("Tie")
    # elif(sc==21 or (su>21 and 1 not in fu)):
    #   to_continue=False
    #   print(f"Computer's cards are {comp[0]} and {comp[1]}")
    #   print("You lose")
    # elif(su>21 and 11 not in user or su>32):
    #   to_continue=False
    #   print(f"Computer's cards are {comp[0]} and {comp[1]}")
    #   print("You Lose")
    elif(su==21):
      to_continue=False
      print(f"Computer's cards are {comp[0]} and {comp[1]}")
      print("BlackJack. You win")
    elif su>21 and 11 not in user:
      to_continue=False
      print(f"Computer's cards are {comp[0]} and {comp[1]}")
      print("Sum more than 21. You lose")
    elif(su>21 and 11 in user): #one ace condition ONLY   
      user.remove(11)
      user.append(1)
      su-=11
      su+=1
      if su>21:
        to_continue=False
        print(f"{su} more than 21. You lose")
    else:
      cond=input("Do you want one more card? Y for yes and N for no ").lower()
      if(cond=="n"):
        print("computer's current cards are")
        print(comp)
        to_continue=False
        if sc>21 and 1 in comp:
            comp.remove(11)
            comp.append(1)
            sc-=11
            sc+=1
        if(sc<=17):
          while sc<=17:
            sc+=pick(comp,1,fc)
            print("computer's current cards are")
            print(comp)
        if sc>21 and 1 not in comp:
            print(f"Your total is {su} and computer's is {sc}. You win")
        elif su<21 and sc<su and  sc<21 :
            print(f"Your total is {su} and computer's is {sc}. You win")
        else:
            print(f"Your total is {su} and computer's is {sc}. You Lose")
        
        
      else:
        su+=pick(user,1,fu)
        if 11 in user:
          su-=11
          su+=1
          user.remove(11)
          user.append(1)
        print(f"Your cards are {user}. Current Score is {su}")
        
      
        
  
      
      
while input("Do you want to play BlackJack Game? ").lower()=="y":
  clear()
  print(logo)
  play()  
  
  
  
  
  
  
  
  
  
  
  
  