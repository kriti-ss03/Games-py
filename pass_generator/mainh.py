#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

ans=""
pass_list=[]
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(0,nr_letters):
  randindx=random.randint(0,25)
  ans+=letters[randindx]
  pass_list.append(letters[randindx])


for i in range(0,nr_symbols):
  randindx=random.randint(0,8)
  ans+=symbols[randindx]
  pass_list.append(symbols[randindx])

for i in range(0,nr_numbers):
  randindx=random.randint(0,9)
  ans+=numbers[randindx]
  pass_list.append(numbers[randindx])
  


print(ans)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


random.shuffle(pass_list)
fans=""
for val in pass_list:
  fans+=val

print(fans)