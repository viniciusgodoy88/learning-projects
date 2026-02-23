'''
Anna Júlia is creating a system to calculate Body Mass Index (BMI) 
and provide basic recommendations. 
The program should receive a person's weight and height and display the 
BMI value, as well as indicate whether they are underweight, 
normal weight, or overweight. Create a program that receives the weight 
(in kg) and height (in meters) and calculates the BMI using the formula: 
BMI = weight / (height * 2). 
Then, display the BMI value and a message indicating whether the person is 
underweight (BMI < 18.5), normal weight (18.5 <= BMI < 25), 
or overweight (BMI >= 25).

'''

weight = float(input("Please, insert your weight (Quilos): "))
height = float(input("Please, insert your height (Meters): "))

bmi = weight/(height**2)
print(f"YOUR BMI IS: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")   
else: 
    print("Overweight")