from Student import Student

student1 = Student("Monique", "Finance", 3.8)
student2 = Student("Zeus", "Chemistry", 3.3)
student3 = Student("Cynthia", "Art", 2.4)
student4 = Student("Ross", "Music", 3.6)
student5 = Student("Abigail", "English", 3.5)
student6 = Student("Geromy", "Math", 2.9)
student7 = Student("Delila", "Biology", 3.1)
student8 = Student("Monica", "Physics", 3.7)
student9 = Student("Larry", "Comedy", 3.5)
student10 = Student("Samantha", "Rhetoric", 2.2)

students = [student1, student2, student3, student4, student5, student6]
results = map(Student.on_honor_roll, students)
print(list(results))