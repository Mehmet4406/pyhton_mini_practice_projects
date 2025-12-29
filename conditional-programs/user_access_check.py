username = input(str("What is your username?"))
password = input(str("What is your password?"))

if username == "user1"   and password == "password1":
    age = int(input("What is your age?"))
    if age >= 18: 
     print("You're considered adult")
    else: 
        print("You're not considered adult")
else:
    print("Your creditentails are not valid")