# 1. Implement palindrome using iterator(for loop).
def reverse_string(str):
    str1 = ""  # Declaring empty string to store the reversed string
    for i in str:
        str1 = i + str1
    print(str1)
    if(str==str1):
        print("It is palindrome")
    else:
        print("It is not a palindrome")

reverse_string("malayalam")

#1.b Implement palindrome using generator mechanism.
#syllabus not covered


#2.2. Sum of 2 digits into output
import functools
n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
res1=[int(x) for x in str(n1)]
res2=[int(x) for x in str(n2)]
result=res1+res2
final=functools.reduce((lambda a,b:a+b),result)
print(final)
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

#4.findout elements duplicate count output in  dict format

str=input("Enter the string:")
dict1={}
for i in str:
    if i in dict1:
        dict1[i]=+1
    else:
        dict1[i]=1
print(dict1)



#5. t1 = (1, 2, 3, "a", "c")
# t2 = ("b", "d", 9, 8, 7)
# Output: (10,10,10,"ab","cd")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
 # reversing the tuple
t3 = t2[2:]
t4 = t2[:2]
t5 = t3+t4
print(t5)

my_result = tuple(map(lambda i, j:i+j, t1, t5))
print(my_result)


#3.program
strsample = "ra@#my!$a"
listSample=list(strsample)
i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1
strOut=''.join(listSample)
print(strOut)



# 6.Write a Python program to remove leading zeros from an IP address.

import re
ip = "216.08.094.0196"
string = re.sub('\.[0]*', '.', ip)
print(string)



#7.
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output = []
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)
# Driver code
print('The original list: ', l)
reemovNestings(l)
print('The list after removing nesting: ', output)

#8th program syllabus not covered