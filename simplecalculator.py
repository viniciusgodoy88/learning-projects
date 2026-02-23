"""
Project: Simple Calculator
Onwer: Vinicius Godoy
Platform: Udemy
Data: 26/05/2025
Teacher: Ryan Aragão
"""

from typing import Any

#User inserted a first number
n1 = int(input("Insert the first number: "))
#User inserted the required option
option = str (input("Insert the operator: "))
#User inserted a second number
n2 = int(input("Insert the second number: "))


#variables and your types
addiction = int
substraction = float
division = float
multiplication = int
potentiation = int
resdivision = float

#If the user required the calculator do the addiction, the funcion is below
if option == "+":
    addiction = n1 + n2
    print("The Addicition between {} + {} = {}".format(n1, n2, addiction))
#If the user required the calculator do the subtraction, the funcion is below
elif option == "-":
    substraction  = n1 - n2
    print("The substraction beetween {} - {} = {}".format(n1, n2, substraction))
#If the user required the calculator do the multiplication, the funcion is below
elif option == "*":
    multiplication = n1 * n2
    print("The multiplication between {} * {} = {}".format(n1, n2, multiplication))
#If the user required the calculator do the potentiation, the funcion is below
elif option == "**":
    potentiation = n1 ** n2
    print("The Potentiation between {}**{} = {}".format(n1, n2, potentiation))
#If the user required the calculator do the rest of division, the funcion is below
elif option == "//":
    resdivision = n1 // n2
    print("The remainder of the division between {} // {} = {}".format(n1, n2, resdivision))
#If the user required the calculator do the division, the funcion is below
else:
    division = n1 / n2
    print("The division between {} / {} = {}".format(n1, n2, division))