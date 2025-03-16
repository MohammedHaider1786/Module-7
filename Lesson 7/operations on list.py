lst = ['Apple', 'Guava', 'Pineapple', 'Grape', 'Blueberry']
print(lst)
print("Length of list: ", len(lst))
print("First element: ", lst[0])
print("Last element: ", lst[-1])

lst.append("Guava")
print("Update list: ", lst)

lst.remove("Pineapple")
print("Update list: ", lst)

lst.sort()
print("Sorted list: ", lst)

lst.pop(2)
print("Updated list: ", lst)

lst.reverse()
print("Reversed list: ", lst)

print("Multiplication on list: ", lst*2)

lst = lst[:4]
print("Sliced List: ",lst)

lst.clear()
print("Update list: ", lst)
