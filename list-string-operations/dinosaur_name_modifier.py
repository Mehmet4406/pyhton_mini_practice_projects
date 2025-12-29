
animal_list = ['ankylosaurus', 'carnotaurus', 'spinosaurus', 'trex', ]

def modify_animal_names(animal_list):
    i = 0 
    while i<len(animal_list):
        word = animal_list[i]
        first_letter = word[0].upper()
        rest = word[1:]
        initials = "_md"
        new_word = first_letter + rest + initials     
        animal_list[i] = new_word
        i += 1

def find_replace_name(animal_list, name):
    i = 0 
    while i < len(animal_list):
        if animal_list[i] == "Spinosaurus_md": 
            animal_list[i] = name 
        i += 1 
    print(animal_list)

modify_animal_names(animal_list)
find_replace_name(animal_list, "Mehmet")    

        
        

