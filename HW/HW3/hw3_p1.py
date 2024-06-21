n = 3
students = list(range(1, n + 1))
index = 0

while len(students) > 1:

    index = (index + 2) % len(students)  # Move two steps forward
    students.pop(index)  # Remove the student who reports 3


last_id = students[0]

print(last_id)
print(5%2, 2%5)

