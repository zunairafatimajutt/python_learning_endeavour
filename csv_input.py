#First 
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

#Vulnerability Scan
import csv
with open ('vuln_scan.csv') as csv_file: #CSV file's name will be written in the brackets, not the one's where we are opening 'that' file.
    csv_reader = csv.reader (csv_file, delimiter = ',') #After csv_file, 'delimiter = ''' will be written.
    line_count = 0 #don't forget to set the line count to 0
    for line in csv_reader: 
        if 'CRITICAL'in line[2].upper():
            print(f"WARNING: Critical vulnerability found! {line[0]} on {line[1]}")

#Brute Force 
import csv
with open ('brute_force.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter = ',')
    line_count = 0 
    failed_count = 0
    for line in csv_reader:#YOU LOOP THROUGH THE READER NOT THE FILE
        if line[2] == 'Failed' and line [0] == '10.0.0.22':
                            failed_count = failed_count + 1
if failed_count >= 3:
    print(f"ALERT: Brute force attack detected from 10.0.0.22! with a failed attempts of {failed_count}")
else:
    print(f"No brute forced attack. There were only {failed_count} failed attempts.")

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

#Practice
import csv
with open ('login.logs.csv') as csv_file:
    csv_reader = csv.reader (csv_file, delimiter = '|')
    line_count = 0
    for line in csv_reader:
        if line[2] == 'Failed':
            print (f"ALERT: failed login for user {line[1]} from IP {line[0]}")

