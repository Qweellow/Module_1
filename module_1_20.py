            # Работа со словарём.
my_dict = {'Max': 1970, 'Alex': 1980, 'John': 1990}
print('Dict: ',my_dict)
print('Existing values: ',my_dict['Max'])
print('Not existing values: ',my_dict.get('Kira'))
my_dict.update({'Jummy': 2000, 'Bob': 2010})
deleted_values = my_dict.pop('Alex')
print('Deleted values: ',deleted_values)
print('Modified dict: ', my_dict)

            # Работа со множествами.
my_set = {1, 1, 5.5,  'pineapple', 5.5}
print('Set: ', set(my_set))
my_set.update(['apple', 18])
my_set.remove(5.5)
print('Modified set: ', my_set)
