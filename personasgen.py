import random

first_names = ['Lama', 'Hila', 'Stephan', 'David', 'Lena']
last_names = ['Osman', 'Mueller', 'Thomas', 'Schultz']
ages = range(18, 101)
streets = ['Berliner str.', 'Hamburger str.', 'Schoener str.']
house_numbers = range(0, 100)
genders = ['M', 'F', 'O']
cities = ['Berlin', 'Hamburg', 'Paris', 'London']
zip_codes = range(10000, 99999)

def generate_persona(num_personas, args):
    personas = []
    for i in range(num_personas):
        persona = {}
        for arg in args:
            if arg == 'first_name':
                persona['first_name'] = random.choice(first_names)
            elif arg == 'last_name':
                persona['last_name'] = random.choice(last_names)
            elif arg == 'age':
                persona['age'] = random.choice(ages)
            elif arg == 'street':
                persona['street'] = random.choice(streets)
            elif arg == 'house_number':
                persona['house_number'] = random.choice(house_numbers)
            elif arg == 'gender':
                persona['gender'] = random.choice(genders)
            elif arg == 'city':
                persona['city'] = random.choice(cities)
            elif arg == 'zip_code':
                persona['zip_code'] = random.choice(zip_codes)
            else:
                print('This is not a valid attribute')

        personas.append(persona)
    return personas
