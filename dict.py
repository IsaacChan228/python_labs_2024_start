import json

# Read the json file
with open('students.json', 'r') as file:
    data = json.load(file)

# Access the dictionary
students = data['students']

# Print the dictionary
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()     # Print a blank line
    