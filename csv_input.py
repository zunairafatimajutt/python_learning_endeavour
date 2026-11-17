import csv

with open('testing.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter = ',') #delimiter = can only hold one character. ',' can also be '|', ' ', '\t'. No delimiter is used for one signle column. 
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            print(f"The headers are {", ".join(line)}")
            line_count += 1 #line_count = line_count +1
        else:
            print(f"\t{line[0]} is taking classes from {line[1]} and is making progress in the {line[2]} course.")

#Modify the code and print only the students taking cybersecurity courses
import csv
with open('testing.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter= ',')
    line_count = 0
    for line in csv_reader:
        if 'Cyber' in line[2]: #make Cyber-> 'cyber' in line[].lower. It will catch 'CYBER', 'Cyber', or even 'cyber'.
            print(f"\t{line[0]} is taking classes from {line[1]} and is making progress in the {line[2]} course.")

#Make a code that only prints port 22 and 443.
import csv
with open('testing.2.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter= '|')
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print (f"\tFound open port at {line[0]} {line[2]}")
            