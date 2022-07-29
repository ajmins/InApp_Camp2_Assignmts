#(CSV - Comma seperatd file
# for data storing in tablura form as plain text, no need of space just , only
# It can be handled in two ways
# using csv.reader module
# and using.readline()
# )
import csv #importing csv module/lib

#opening csv file
file = open("mycsvfile.csv")
#using csv.reader to read the file object
csvreader = csv.reader(file)

#method: "next", to read every lines
#declaring empty header and rows list
header = []
rows = []

#next() : to read the current line and stop at the start of next line
header = next(csvreader)
print(header)

#read the rows below header
for row in csvreader:
    rows.append(row)
print(rows)
#close the file handler
file.close()

#using with statement

rows1 = []
with open("mycsvfile.csv","r") as file1:
    csvreader1 = csv.reader(file1)
    header1 = next(csvreader1)
    for row1 in csvreader1:
        rows1.append(row1)

print(header)
print(rows)

print("-----Eg-------")
#without the csv library
with open("mycsvfile.csv","r") as file2:
    content = file2.readlines()

#to strip the new line character
content = [i.strip() for i in content]
#header will be the first index value
header2 = content[:1]

rows2 = content[1:]

print(header2)
print(rows2)

print("-----Eg-------")
#writing to a csv file using csv.writer
header3 = ['Name','Experience','Salary']
data = [['Ajmi',9,30000],['Anu',8,25000],['Den',5,12345]]

with open("mycsvfile2.csv","w",newline="") as file3:
    csvwriter = csv.writer(file3)
    csvwriter.writerow(header3) #write the row contents using writerow()
    csvwriter.writerows(data)#write the row contents using writerows()

print(header3)
print(data)