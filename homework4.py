immutable_var = (1, "apple", 4, False)
print(immutable_var)
immutable_var [1] = "peach"
print(immutable_var) #значение не изменяется потому что в картеже нельзя менять включенные в него элементы
mutable_list = [1, 2, 3, 4]
mutable_list [1] = 4
print(mutable_list)
