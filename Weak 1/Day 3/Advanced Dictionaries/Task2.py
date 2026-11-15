students_dicts = [{"name": "Riya", "marks": 88}, {"name": "Aman", "marks": 95}, {"name": "Sara", "marks": 91}]

top_student = students_dicts[0]
for student in students_dicts:
    if student["marks"] > top_student["marks"]:
        top_student = student

print("Top student:", top_student)