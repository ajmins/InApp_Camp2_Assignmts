#python REGEX
#refer for more : https://www.w3schools.com/python/gloss_python_regex.asp
# https://www.programiz.com/python-programming/regex
import re
 

txt = "bits of paper bits"
print(txt.find('of')) #5
x =re.findall("bi", txt)
print(x)

#['bi', 'bi']

y = re.search("bi", txt)
print(y)
#<re.Match object; span=(0, 2), match='bi'>

#print(x.span())
#print(x.string)
#print(x.group())
#------------------------------------------------------------------------#
w = re.split(" ", txt)
print(w) #['bits', 'of', 'paper', 'bits']

u = re.split(" ", txt, 1)
print(u) #['bits', 'of paper bits']

t = re.sub(" ", "-", txt)
print(t) #bits-of-paper-bits

txt2 = "hello world"
p = re.findall("[a-m]", txt2)
print(p) #['h', 'e', 'l', 'l', 'l', 'd']

txt3 = "James bond is 007"
q = re.findall("\d", txt3)
print(q) #['0', '0', '7']

r =  re.findall("he..o", txt2)
print(r) #['hello']
#------------------------------------------------------------------------#
#begin search
#metacharacter ^
s =  re.findall("^hell", txt2)
print(s) #['hell']
#these  will check for the pattern

#special sequence \A
o =  re.findall("\Ahell", txt2)
print(o) #['hell']
txt4 = "Watt invented James theso engine"
s1 =  re.findall("\AJam", txt4)
print(s1) #[]
#these  will check for the  pattern

#end search
#metacharacter $
v =  re.findall("world$", txt2)
print(v) #['world']

#special sequence \b at the beginning, end and middle of word
s2 =  re.findall(r"\bworld", txt2)
print(s2)  #['world']

s3 =  re.findall(r"\bthe", txt4)
print(s3) #['the']
#------------------------------------------------------------------------#
#mathcing sn email within a string using special sequences
txt5 = "hello text@gmail.com how are you?"
#regular expression to match email
#check for non space chars before and after '@' , for that use \S
regex = r'\S+@\S+'
s4 =  re.findall(regex, txt5)
print(s4) #['text@gmail.com']

regex1 = r'\S+@\S'
s5 =  re.findall(regex1, txt5)
print(s5) #['text@g']
#------------------------------------------------------------------------#
