def mark_statistics(marks):
    return min(marks), max(marks), sum(marks) / len(marks)

student_marks = [85, 92, 78, 90, 88]
lowest, highest, average = mark_statistics(student_marks)

print(f"Lowest: {lowest}, Highest: {highest}, Average: {average}")