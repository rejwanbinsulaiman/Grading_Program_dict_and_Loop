student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades to student_grades.👇
for student in student_scores:
    grade = student_scores[student] 
    grade = int(grade)
    if grade > 90:
        student_grades[student] = "Outstanding"
    elif grade > 80:
        student_grades[student] = "Exceeds Expectations"
    elif grade > 70:
        student_grades[student] =  "Acceptable"
    else:
        student_grades[student] =  "Fail"
    #print(grade)

print(student_grades)