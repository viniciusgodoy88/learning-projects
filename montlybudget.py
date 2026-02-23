'''
Carlos wants to monitor his monthly budget to avoid overspending. 
He has set a spending limit of R$3,000.00 and needs a program to 
help him control his expenses. 
The program should receive the total expenses incurred and 
inform him whether he has exceeded the limit or is still within his budget.
'''

limit = 3000.0
budget = float(input("Insert your budget: "))

if budget > limit:
    print("Warning! You have exceeded your budget limit. ")
else:
    print("You are still within the limit. ")