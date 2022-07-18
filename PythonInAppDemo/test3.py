#python REGEX
#refer for more : https://www.w3schools.com/python/gloss_python_regex.asp
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


#metacharacter ^
s =  re.findall("^hell", txt2)
print(s) #['hell']
#these  will check for the pattern
o =  re.findall("\Ahell", txt2)

#special sequence \A
print(o) #['hell']
txt4 = "Watt invented James the engine"
s1 =  re.findall("\AJam", txt4)
print(s1) #[]
#these  will check for the  pattern

#metacharacter $
v =  re.findall("world$", txt2)
print(v) #['world']

#special sequence \b
s2 =  re.findall(r"\bworld", txt2)
print(s2) 