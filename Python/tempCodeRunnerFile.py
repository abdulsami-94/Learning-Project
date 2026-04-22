students = {'Alice': 85, 
            'Bob': 92, 
            'Charlia': 78, 
            'Diana': 95, 
            'Eve': 88
            }

top_students = max(students, key=students.get)
print(f'Top students: {top_students} with {students[top_students]} marks')