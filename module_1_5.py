immutable_var = 1,2,'a','b'       # class tuple
print(immutable_var)
# immutable_var[0] = 44  # TypeError: 'tuple' object does not support item assignment
mutable_list =[1,2,'a','b','c']   # class list
mutable_list[4] = 'Modified'
print(mutable_list)