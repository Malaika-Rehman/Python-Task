text = input("Enter a string: ")

search = input("Enter the character or word to find: ")

index = text.find(search)
if index != -1:
    print(f"'{search}' found at index {index}")
else:
    print(f"'{search}' not found in the string.")