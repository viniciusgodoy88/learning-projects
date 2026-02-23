'''
Mariana is responsible for granting access to the office 
and needs a program to check if employees can enter. 
To do this, she will use the current time. The office only 
allows access between 8 AM and 6 PM. Create a program that receives the 
current time as input (in 24-hour format) and displays a 
message indicating whether access is allowed or denied.

'''

hour = int(input("Digite a hora atual (Formato 24 Horas): "))

if 8 <= hour < 18:
    print("Access permitted")
else:
    print("Access Denied")