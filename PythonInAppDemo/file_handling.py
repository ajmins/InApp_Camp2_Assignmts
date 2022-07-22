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
myFile = open("myfile.txt","r")
print(myFile.read())
"""
Just a text file!

Another line!
"""
#located at differnt drive 
myFile2 = open("J:\\myfile2.txt","r") 
print(myFile2.read())
"""
Hi, am a new file in another directory
"""
#to return fst 5 characters
myFile = open("myfile.txt","r")
print(myFile.read(5)) 
"""
Just 
"""
#to return fst and scnd lines
print(myFile.readline()) 
print(myFile.readline()) 
print(myFile.readline()) 
print(myFile.readlines()) #['\n', 'jack and jill\n', ' went up the hill\n', ' to fetch a \n', ' pale of water']
print(myFile.readline())