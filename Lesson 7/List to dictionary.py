def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, "James", 'v'], [2, "Michal", 'v'], [3, "Ronaldo", 'vi'], [4, "Lebron", 'vi'], [5, "Harrison", "vii"]]

print("\nOriginal list of students: ")
print(students)
print("\nConverted list to a dictionary: ")
print(list(students))
    