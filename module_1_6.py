my_dict = {'Anna': 2002, 'Boris': 1999, 'Camila': 2001, 'Den': 1988} # dictionary created
print('Dict: ',my_dict)
print('Existing value: ', my_dict.get('Anna'))
print('Not existing value: ', my_dict.get('Sam'))
my_dict.update({'Irena': 2003, 'Sam': 1999})                         # dictionary updated
a = my_dict.pop ('Sam')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)                              # dictionary modified


my_set = {1, 33, 'Apple', 42.314, (7,8,9), 1, 'Apple', (7,8,9)}      # set created
print('Set:', my_set)
my_set.add(22)
my_set.add('Perch')                                                  # elements added
my_set.remove('Apple')                                               # element deleted
print('Modified set:', my_set)                                       # set modified