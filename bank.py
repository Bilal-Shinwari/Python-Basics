'''Write a program that opens a bank account for users. The program should ask and store the following data of the user.
1. Name
2. Initial deposit amount

At the end, the user withdraws an amount equal to 10% of the initial deposited amount, and the program will display a reciept containing:
a. The name of the customer
b. His remaining balance.
c. Cash withdrawn  
For example: Ali, you have withdrawn 200.0 PKR. Your remaining balance is: 1800.0'''

name=input("Enter your name : ")
balnace =float(input("Enter your initial deposite : "))

withdraw=balnace   * 0.1 
balnace =balnace - withdraw

print("{0},you have withdraw {1} PKR .Your remaining balance is {2} PKR".format(name,withdraw,balnace) )

