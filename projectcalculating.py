'''
Camila is organizing a project and needs to calculate 
the total time required to complete three activities: A, B, and C.

However, if any activity has a negative number of days, 
the code should warn that the entered values ​​are invalid 
and not calculate the total.

Write a program that receives the number of days 
for three activities and displays the total project time. 
If any value is negative, show an error message.

'''

activity_A = int (input("Please specify the days for activity A: "))
activity_B = int (input("Please specify the days for activity B: "))
activity_C = int (input("Please specify the days for activity C: "))
dias = 0

if (activity_A >= 0 and activity_B >= 0 and activity_C >= 0):
    total_time = activity_A + activity_B + activity_C
    print(f"The total project time is {total_time} days.")
else: 
    print("Error: The days can't be negative.")