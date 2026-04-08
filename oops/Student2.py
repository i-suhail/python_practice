class Student2:
    college_name = "AMU"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def marks(self):
        print(self.marks)
    def Welcome(self):
        print("Welcome Student", self.name)

s1 = Student2("Mubeen", 97)
s2 = Student2("Muneer", 79)
s3 = Student2("Muhsin", 67)
s4 = Student2("Musa", 96)
print(s1.name, s1.marks)
print(s2.name, s2.marks)
print(s3.name, s3.marks)
print(s4.name, s4.marks)
s1.Welcome()
s2.Welcome()
s3.Welcome()
s4.Welcome()
