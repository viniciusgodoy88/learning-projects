'''
Lucas is developing a game and needs a feature that checks 
if a number is even or odd. This check will be used to define
different actions within the game. 
rite a program that receives an integer and displays a 
message indicating whether it is even or odd.
'''

parity = int(input("Please insert the number: "))

if parity %2 == 0:
    print("Pair number ")
else: 
    print("Odd number ")

