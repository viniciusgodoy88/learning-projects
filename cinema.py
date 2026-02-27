age = int(input("Please insert your age: "))
student = bool (input("You're student (T(true)/F(false)): "))
is_student = True
under_eighteen = False

total_price = 40
price = total_price / 2

type(is_student)

if age <18 or under_eighteen:
 print("Half price applied!, The currently value is: ",price)

else:
 print ("Your price is: ",total_price)

