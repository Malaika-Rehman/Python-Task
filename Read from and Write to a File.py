with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python makes file handling easy!")

with open("sample.txt", "r") as file:
    content = file.read()

print("File content:\n", content)
