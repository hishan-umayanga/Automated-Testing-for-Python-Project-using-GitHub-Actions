num_a= float(input("Enter number "))
op=input('Enter "+", "-", "*", "/" ')
num_b = float(input("Enter number "))

def add(num1,num2):
      return num1+num2

def sub(num1,num2):
      return num1-num2

def mul(num1,num2):
      return num1*num2

def divide(num1,num2):
      return num1/num2

if op == '+':
      print(f"{num_a} {op} {num_b} = {add(num_a,num_b)}")

elif op == '-':
      print(f"{num_a} {op} {num_b} = {sub(num_a,num_b)}")

elif op == '*':
      print(f"{num_a} {op} {num_b} = {mul(num_a,num_b)}")
elif op == '/':
      print(f"{num_a} {op} {num_b} = {divide(num_a,num_b)}")

else:
      print("Enter correct operator in the given")


print("the is the end ")