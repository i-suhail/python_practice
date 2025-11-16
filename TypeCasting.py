name = "S"
age = 21
is_student = True
gpa=8.06
print(gpa, type(gpa))
gpa = int (gpa)
print(gpa, type(gpa))
age = str (age)
age += "1"
print("added one to age at last ",age, type(age))
name = bool(name)
print(name) # GIVES FALSE ONLY WHEN STR IN EMPTY,CAN BE USED IN HANDLING USER I/P