from art import logo

print(logo)

def add(a, b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a,b):
  return a/b


dict={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  to_continue=True
  n1=float(input("Give first number "))
  while(to_continue): 
    opt=input("provide operation ")
    n2=float(input("Give second number "))
    ans=dict[opt](n1,n2)
    print(f"{n1} {opt} {n2}={ans}")
  
    flag=input(f"Type Y to continue with {ans} and N to exit and start new ").lower()
    if(flag=="n"):
      to_continue=False
      calculator()
    else:
      n1=ans

calculator()