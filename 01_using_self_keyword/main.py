class Student:
    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

Student1 = Student("Muzammil Ayoub", 90)
Student1.display()