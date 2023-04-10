from art import logo
from art import vs
import random
from replit import clear
print(logo)

from game_data import data

def compare(indx1,indx2,inp,score):
  if data[indx1]['follower_count'] < data[indx2]['follower_count']:
    if(inp=='B'):
      clear()
      score+=1
      print(logo)
      print(f"You're right! Current score: {score}.")
      ppl(indx2,score)
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
  else:
     if(inp=='A'):
       clear()
       score+=1
       print(logo)
       print(f"You're right! Current score: {score}.")
       ppl(indx1,score)
     else:
       clear()
       print(logo)
       print(f"Sorry, that's wrong. Final score: {score}")
  # print(score)
  return score
  
  
def ppl(indx,score):
  
  print(f"Compare A: {data[indx]['name']}, a {data[indx]['description']}, from {data[indx]['country']}.")  

  indx2=indx
  while indx2==indx:
    indx2=random.randint(0,len(data)-1)

  print(vs)
  print(f"Compare B: {data[indx2]['name']}, a {data[indx2]['description']}, from {data[indx2]['country']}.")  
  
  inp =input("Who has more followers? Type 'A or 'B' ")
  s=compare(indx,indx2,inp,score)
  score=s
  # if(s==score and inp=='A'):
  #   ppl(indx,s)
  # elif (s==score and inp=='B'):
  #   ppl(indx2,s)
  # else:
  #   return
  
  
  

a=random.randint(0,len(data)-1)
ppl(a,0)