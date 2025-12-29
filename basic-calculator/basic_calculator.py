first_value = int(input("Enter first value"))
second_value = int(input("Enter secon value"))

operation = int(input("What operation would you like to perform? 1 to add, 2 to subtract, 3 to divide, and 4 to multiply."))

if operation == 1:
    print(first_value + second_value)

elif operation == 2: 
    print(first_value - second_value)

elif operation == 3: 
    print(first_value / second_value)

elif operation == 4: 
    print(first_value * second_value)

else:
    print("incorrect entry")