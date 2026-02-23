'''
Lucas works in IT and needs to ensure that 
the temperature of a server room does not exceed 25°C.

He wants a program that receives the current temperature 
as input and, if necessary, displays an alert message.

'''

temperature = float(input("Insert the temperature servers: "))

if(temperature < 25):
    print("Congratulations, safe temperature! ")
else: 
    print("***WARNING***, PLEASE CHECK THE SERVERS! ")