students = [
    {"name": "Malaika", "age": 20},
    {"name": "Sara", "age": 22},
    {"name": "Hamza", "age": 16}
]
sorted_students = sorted(students, key=lambda x: x['age'])

print("Students sorted by age:")
for student in sorted_students:
    print(student)
