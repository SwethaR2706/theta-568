students = {
   1:  {"name":"google", "age": 20},
   2:  {"name":"deloitte", "age": 23},
   3:  {"name":"aws", "age": 31},
   4:  {"name":"flipkart", "age": 26},
   5:  {"name":"tcs", "age": 27},
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")