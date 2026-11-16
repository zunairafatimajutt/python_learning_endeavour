student_name:str
student_name=input("Enter your name")
student_age:int
student_age=input("Enter age")
gpa: float
gpa=input("tell me you're gpa")
enrollment: bool
enrollment=input("type 'yes' if you are. type 'no' if you aren't")
if enrollment == "yes":
    print("Welcome back", student_name, "age", student_age, "with a gpa of", gpa)
else:
    print("error, you are not authorised")