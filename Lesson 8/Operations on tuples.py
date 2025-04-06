#Empty tuple
my_tuple=()
print(my_tuple) 
#Tuple having integers
my_tuple=(1,2,5,6)
print(my_tuple)
#Tuple with mixed datatypes
my_tuple=("Cr7", 3, "eight")
print(my_tuple)
#nested tuple
my_tuple=("Horse", [1, 2, 3, 7, 8 ])
print(my_tuple)
#Accessing tuple elements using indexing
my_tuple=('R', 'o', 'n', 'a', 'l', 'd', 'o')
print(my_tuple[0])
print(my_tuple[6])
#nested tuple
n_tuple=("Cat", [7, 5, 9], (2, 4, 6) )
#nested index
print(n_tuple[0][1])
print(n_tuple[1][2])
#Slicing
print("Sliced :", my_tuple[1:4])
#Iterating through tuple
for letter in(my_tuple):
    print("Hello", letter)