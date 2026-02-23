'''
A teacher needs a program that helps calculate students' final averages 
and informs them whether they passed, need remedial classes, or failed. 

The rules are:
Average >= 7: Passed
5 <= Average < 7: Remedial classes
Average < 5: Failed

Write a program that receives three grades as input and 
calculates the final average. Based on the average, display the student's 
status.

'''

M1 = float(input("Insert the first exam grade: "))
M2 = float(input("Insert the second exam grade: "))
M3 = float(input("Insert the Third exam grade: "))

Average = (M1+M2+M3)/3

print(f"Your Average is: {Average:.2f}")

if Average >= 7:
    print("Congratulations, you're passed, Enjoy your rest! ")
elif 5 <= Average < 7:
    print("Remedial classes")
else: 
    print("Sorry, you're failed")