immutable_var = (1, 3.14, "Hello", True)
print(immutable_var)
#immutable_var[0] = 2
#Кортеж является неизменяемым (immutable) типом данных в Python. Это означает, что после создания кортежа его элементы нельзя изменить.
mutable_list = [1, 3.14, "Hello", True]
mutable_list[0] = 2
print(mutable_list)