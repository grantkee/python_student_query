from Student import Student

student1 = Student("Monique", "Finance", "Business", 3.8)
student2 = Student("Zeus", "Chemistry", "STEM", 3.3)
student3 = Student("Cynthia", "Art History", "Art", 2.4)
student4 = Student("Ross", "Music", "Art", 3.6)
student5 = Student("Abigail", "English", "English", 3.5)
student6 = Student("Geromy", "Math", "STEM", 2.9)
student7 = Student("Delila", "Biology", "STEM", 3.1)
student8 = Student("Monica", "Physics", "STEM", 3.7)
student9 = Student("Larry", "Comedy", "Art", 3.5)
student10 = Student("Samantha", "Rhetoric", "English", 2.2)
student11 = Student("Bob", "Writing", "English", 3.9)

students = [student1, student2, student3, student4, student5, student6]
results = map(Student.on_honor_roll, students)
print(list(results))