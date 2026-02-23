'''
Project: Calculator V2
Onwer: Vinicius Godoy
Platform: Udemy
Data: 31/05/2025
Teacher: Ryan Aragão
'''

def welcome():
    print("Welcome to Calculator V2! ")

while True:
    welcome()
    first_numero = int(input("Please insert the first value: "))
    second_numero = int(input("Please insert the second value: "))
    
    print('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    ''')
    
    option = int(input("Insert the required option: "))
    
    if option == 1:
        addition = first_numero + second_numero
        print("The addition is: ", addition)
    elif option == 2:
        subtraction = first_numero - second_numero
        print("The subtraction is: ", subtraction)
    elif option == 3:
        multiplication = first_numero * second_numero
        print("The multiplication is: ", multiplication)
    elif option == 4:
        if second_numero != 0:
            division = first_numero / second_numero
            print("The division is: ", division)
        else:
            print("Cannot divide by zero.")
    elif option == 5:
        print("Exiting the program.")
        break
    else:
        print("Option not found, please try again!")