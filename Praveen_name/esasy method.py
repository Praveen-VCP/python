import random

departments = ['EEE', 'ECE', 'MECH', 'CSC']
students_per_dept = 10

data = {}
for dept in departments:
    data[dept] = []
    for i in range(students_per_dept):
        student = {
            'name': f'Student_{dept}_{i+1}',
            'age': random.randint(18, 24),
            'sem': random.randint(1, 8),
            'mark': random.randint(50, 100),
            'place': f'Place_{random.randint(1, 5)}',
            'amaa' : random.randint(18,89),

        }
        data[dept].append(student)

# Calculate total marks for each department
dept_marks = {dept: sum(student['mark'] for student in students) for dept, students in data.items()}

# Find the winning department
winning_dept = max(dept_marks, key=dept_marks.get)

print("Department-wise total marks:", dept_marks)
print("Winning Department:", winning_dept)























