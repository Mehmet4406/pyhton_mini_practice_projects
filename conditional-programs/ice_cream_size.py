price = float(input("How much would you like to pay for the ice cream?: "))
name = str(input("What's your name?: "))

if 1 < price <= 2:
    print("Small ice cream, $" ,price,",",name) 

elif 2 < price <= 5:
    print("Medium ice cream, $" ,price,",",name) 

elif 10 <= price :
    print("Large ice cream, $" ,price,",",name) 

else:
    print("Sorry, we don't have a size for $",price) 


