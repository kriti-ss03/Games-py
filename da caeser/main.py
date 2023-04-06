from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


 
def ceaser(text,shift,direction): 
  if direction=="decode":
      shift*=(-1)
  ans=""  
  for letter in text:
    if letter not in alphabet:
      ans+=letter
      continue;
    indx=alphabet.index(letter)
    nindx=indx+shift
    newletter=alphabet[nindx%26]
    ans+=newletter
  print(ans)

 
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

flag=True
while(flag==True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  ceaser(text,shift,direction)
   
  str=input("Type yes to continue & no to end ")
  if(str.lower()=="no"):
      flag=False
      print("Byem Byem")
  else:
    print("hemlo again")