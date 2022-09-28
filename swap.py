#swaping numbers with different methods 

#1st Method 




num1=10
num2=5

temp=num1 #taking another variable as temp
num1=num2
num2=temp

print("num1 =",num1)
print("num2 =",num2)

#2nd method only used in python

a=5
b=6

a,b=b,a

print(f"a = {a} and b = {b}")

#3rd method 

x=17
y=13

x=x^y
y=x^y
x=x^y

print(f"x = {x} and y = {y}")

