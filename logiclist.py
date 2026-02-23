'''
Logic Exercise
Onwer: Vinicius Godoy
Data: 27/05/2025
Plataform: Udemy
Professor: Ryan Aragão

'''

list = ['Vinicius', 'Lethicia', 'Olivete', 'Marcia', 'Julia', 'JP', 'Junior', 'Idália']

while True:
    print('''
        1. Including People
        2. Search People
        3. Exit
    ''')
    choice = int(input("Insert the required option: "))
    
    if choice == 1:
        people = input("Insert the name to include: ")
        list.append(people)
        print("People inserted successfully!")
    
    elif choice == 2:
        people = input("Insert the name to search: ")
        if people in list:
            print("The person is in the list!")
        else:
            print("Sorry, the person isn't in the list.")
    
    elif choice == 3:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid option. Please try again.")