passes = 0
failures = 0
student = 1

while student <= 10:
    exam_result = input("Next Exam Result (passes/failures):")
   
    if exam_result == "passed":
        passes = passes + 1
    else:
        failures = failures + 1

    student = student + 1    

print("The Number of Passes:", passes)
print("The number of Failures:", failures)

if passes >= 8:
   print("Raise Tuition.")

successful_pings = 0
failed_pings = 0
attempt = 1
while attempt <=5:
    ping_result = input("The Result of the Ping (up/down):")
    if ping_result == "up":
        successful_pings = successful_pings + 1
    else:
        failed_pings = failed_pings + 1
    attempt = attempt + 1

print("The Number of Seccesful Pings:", successful_pings)
print("The Number of Failed Pings:", failed_pings)

if failed_pings>=3:
    print("Warning: Server Unstable.")

z = input("Enter a Number:")

if int(z)==10:
    print("YOU'RE A TEN")
elif int(z)>5:
    print("Number is greater than 5. Period.")
else:
    print("Number is less than 5. Period.")

word = ["hellow, hellow, hellow, hellow, hellow"]

for i in word:
    print("i\n")   