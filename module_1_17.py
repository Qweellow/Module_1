immutable_var = 1, 0.5, 'String'
print(immutable_var)
# immutable_var[1] = 1.5 # tuple то есть кортеж, не принял изменение объекта, потому что в отличии от списка, кортеж неизменяем.
mutable_list = [10, 5.5, 'String']
mutable_list.extend(['String2'])
print(mutable_list)