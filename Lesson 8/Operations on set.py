my_set={1,2,2,2,3,4,4,5}
print("Set :", my_set)

my_set.add(5)
print("Update Set:", my_set)

set_1 = my_set
set_2 = {1,2,2,6}

print("\nSet 1", set_1)
print("Set 2", set_2)
print("Difference")
print(set_1.difference(set_2))
print("Symmetric Difference")
print(set_1.symmetric_difference(set_2))