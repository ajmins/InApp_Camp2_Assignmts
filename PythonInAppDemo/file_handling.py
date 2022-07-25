#(python File Handling
# open() : 2 parameters->filename and mode
# 4 modes:
#   r -Read, error if not exits
#   a -Append, create a new file if not exists
#   w -Write, create a new file if not exists
#   x -Create, error if not exists
# 
# in addition , file handling as binary or text mode
# t -Text - default value Text mode
# b -Binary - binary mode (image))

#create a new file named myfile.txt and open using read mode
#"myFile" is the file handler
"""

myFile = open("myfile.txt","r")
print(myFile.read())

Just a text file!

Another line!

#located at differnt drive 
myFile2 = open("J:\\myfile2.txt","r") 
print(myFile2.read())

Hi, am a new file in another directory

#to return fst 5 characters
myFile = open("myfile.txt","r")
print(myFile.read(5)) 
#myFile.close()

Just 

#to return fst and scnd lines
print(myFile.readline()) 
print(myFile.readline()) 
print(myFile.readline()) 
print(myFile.readlines()) #['\n', 'jack and jill\n', ' went up the hill\n', ' to fetch a \n', ' pale of water']
print(myFile.readline())


#open in read mode, appended the lines
myFile = open("myfile.txt","a")
#write() method to write text/data
myFile.write("\n Humpty Dumpty sat on a wall")
myFile.close()

myFile2 = open("myfile.txt","r")
print(myFile2.read())
myFile2.close()

#write mode
#contnets will be replaced, so beware
myFile = open("myfile2.txt","w")
#write() method to write text/data
myFile.write("Humpty Dumpty sat on a wall\n")
myFile.close()

#x mode, create a new file


#(checking the file positions)
myFile = open("myfile2.txt","r")
print("file pointer is now at ",myFile.tell()) 
#output

file pointer is now at  0

myFileContents =myFile.readlines()
print("after reading file pointer is now at ",myFile.tell()) 
print(myFileContents)
myFile.close()

#output

after reading file pointer is now at  29

myFile = open("myfile2.txt","r")
print(myFile.readline()) 
print("after reading file line by line pointer is now at ",myFile.tell()) 
print(myFileContents)
myFile.close()
#output

print("------------#########---------------")
myFile3 = open("myfile2.txt","r")
print("file pointer is now at ",myFile3.tell()) 
myFile3.seek(30)
print("after reading file pointer is now at ",myFile3.tell()) 
myFileContentsList =myFile3.readlines()
print("after reading file line by line pointer is now at ",myFile3.tell()) 
print(myFileContentsList)
myFile3.close()
"""

#to modify files, rename, delete, folder manipulation etc
import os
from unittest import result 
if os.path.exists("myFile2.txt"):
    os.rename("myFile2.txt", "myNewFile.txt")
    print("Rename Success")
else:
    print("The file do not exists")


#delete a file
if os.path.exists("myFile.txt"):
    os.remove("myFile.txt")
    print("Removed Successfully")
else:
    print("The file do not exists")


#folder manipulation in Python
#(mkdir() - to create new direectpry
# Getcwd() - get current working dir
# chdir() - to change current working diectory
# )

#to create new directory 
#os.mkdir("mydir")

#to display cwd
print(os.getcwd()) #C:\Users\Ajmi\Camp2\PythonInAppDemo

#to change cwd
#os.chdir("mydir")
print(os.getcwd()) #C:\Users\Ajmi\Camp2\PythonInAppDemo\mydir

#to delete directory 
#os.rmdir("mydir")

#to go back the previous directory
#(os.chdir("..")
print(os.getcwd())

#to list all files and folders
result = os.listdir(os.getcwd())
print(result)



#write output of a program into a file.
#check_call() : from module subprocessto executea pytho script and write the output of that script to a file
#one python file executes the script file.py and writes its output to the text file sample.txt with will automatcally close file pointer once completed
#for that run an external python file(fileoutputsave.py) and save its results to another file as txt
import subprocess
with open("sample.txt", "wb") as f:
    subprocess.check_call(["python","fileoutputsave.py"], stdout=f)






