my_dict = {}

my_dict = {1: 'apple', 2: "ball"}

my_dict = {'name': 'john', 1: [2, 4, 3]}

my_dict = {'name': 'James', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 27
print(my_dict)

my_dict['address'] = 'Karachi'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("address: ", my_dict.get('address'))

my_dict.clear()
print(my_dict)

