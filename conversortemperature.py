print("Temperature Conversor!")

# Criando a função
def conversorCforF(celsius):
    return (celsius * 9/5) + 32

# Entrada de dados
celsius = float(input("Insert the Degrees temperature in Celsius: "))

# Chamando a função
f = conversorCforF(celsius)

# Exibindo o resultado
print("Temperature in Fº:", f, "ºF")