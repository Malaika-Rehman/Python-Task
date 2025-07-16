numbers = [1, 2, 3, 4, 2]

if len(numbers) != len(set(numbers)):
    print("The list contains duplicates.")
else:
    print("All elements are unique.")