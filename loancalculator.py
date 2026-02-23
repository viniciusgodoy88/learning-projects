'''
Docstring for loancalculator
'''

income = float(input("Please insert your income: "))
installment = float(input("Please insert your installment: "))

if income > 2000 and installment <=0.3 * income:
    print("Loan Approved! ")
elif income < 2000: 
    print("Loan Denied, your income is insuficient")
else:
    print("Loan Denied, the installment is more 30% for your income")