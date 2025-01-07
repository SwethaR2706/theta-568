students = {
   1:  {"name":"Swetha", "marks": 20},
   2:  {"name":"Nikki", "marks": 23},
   3:  {"name":"Gorre", "marks": 31},
   4:  {"name":"Keerthi", "marks": 26},
   5:  {"name":"Minty", "marks": 27},
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Marks: {details['marks']}")