import hangman_art
import hangman_words
import random 

print(hangman_art.logo)

str=random.choice(hangman_words.word_list)
# print(str)

blnk=[]
alr_guessed=[]
lives=6

for i in range(0,len(str)):
  blnk.append('_')

print(f"{' '.join(blnk)}")
end_of_game = False


while end_of_game==False:
  
  guess=input("Guess a letter ")
  guess.islower()
  
  if guess in alr_guessed:
    print(f"You've already choosen the {guess} letter")
  
  else:
    alr_guessed.append(guess)
    #Check guessed letter
    for i in range(0,len(str)):  
     
      if(guess==str[i]):
        blnk[i]=guess
  
    
  
    if guess not in str:
      print(f"{guess} is not present in word")
      lives-=1
      print(hangman_art.stages[lives])
      
      if lives==0:
        end_of_game = True
        print("You lose")
        print(f"The correct word is {str}")
        break
  
    print(f"{' '.join(blnk)}")
    
    if '_' not in blnk:
        end_of_game = True
        print("You win.")
      
  

  
    
  
    
    
    
  
    