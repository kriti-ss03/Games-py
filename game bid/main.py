from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
all_bid=[]
# list of dictionaries
def add(name,bid):
  new_item={}
  new_item["name"]=name
  new_item["bid"]=bid
  all_bid.append(new_item)
  



chalo=True
# also don't need to make arr of dictionaries just see if it's max or not n if max then store otherwise skip
while(chalo):
  print(logo)
  name=input("NAME? ")
  print(name)
  bid=int(input("bid val? Rs."))
  
  add(name,bid)
  flag=input("yes to continue or no to exit ")
  
  if(flag=="yes"):
    clear()
  else:
    chalo=False
    maxi=0
    for item in all_bid:
      print(item)
      if maxi<item["bid"]:
        maxi=item["bid"]
        name=item["name"]
  
    print(f"{name} put the maxm bid of {maxi}")