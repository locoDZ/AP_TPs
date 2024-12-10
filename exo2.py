temperature = int(input("Please type in the temperature: "))

if temperature < 0:
    print("It's freezing!")
    print("It's cold!")
    print("It's cool!")
elif temperature < 10:
    print("It's cold!")
    print("It's cool!")
elif temperature < 20:
    print("It's cool!")
print("Stay safe!")