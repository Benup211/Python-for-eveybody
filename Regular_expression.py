#Regular Expression
# ^ beginning of the line
# $ end of the line
# . matches any character
# \s matches whitespace
# \S matches any non-whitespace
# * repeat character zero or more times
# *? repeat character zero or more times (non-greedy)
# + repeat character one or more times
# +? repeat character one or more times (non-greedy)
# [aeious] matches single character in linkedlist
# [^XYZ] matches a single character not in a linked list
# [a-z0-9] set of character included in the list
# ( indicate where string extraction start
# ) indicate where string extraction end
import re
a=['X-hello-world!','X-Hello World!','X-HELLO-WORLD!']
#start with X between any no .of character and end with !
print("start with X between any no .of character and end with !")
for i in a:
    if re.search('^X.*!',i):
        print(i)
    else:
        print(i,"not found")
# Start with X and between non white space value and end with !
print("Start with X and between non white space value and end with !")
for i in a:
    if re.search('^X\S+!',i):
        print(i)
    else:
        print(i,"not found")
#extracting value from string
print("Extract number from string")
x="My favourite nunmber is 2 and 13"
y=re.findall('[0-9]+',x) #extract number
print(y)
print("Extract aeiou from string")
z=re.findall('[aeiou]+',x)#extacting aeiou from string
print(z)
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)