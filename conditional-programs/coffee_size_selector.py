message_list = ['Small', 'Medium', 'Large']
questions = ['How much would you like to pay for a cup of coffee?']

def get_coffee_size(lst,questions):
    price = float(input(questions[0]))
    if price <= 3:
        print(lst[0])
    elif 3 < price < 4:
        print(lst[1]) 
    else:
        print(lst[2])

get_coffee_size(message_list,questions)