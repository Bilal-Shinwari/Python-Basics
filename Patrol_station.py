'''
Write a python program that finds out how much petrol (in liter) has been filled up in a car. 
Customers will be asked how much petrol they want to fill up. 
Given that 1L = 250.10 PKR.
The Program should print a reciept, for example:
You filled up 13.32 L of petrol of price = 150.1 today.
'''

price = 290.34

to_fill=float(input("How much do you want to fill up : "))

litters=round(to_fill/price,2)

print("You filled up {0} L of petrol of price = 250.10 today ".format(litters))
