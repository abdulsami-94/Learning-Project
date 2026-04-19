# SLIP 1
# 1 - Area of rectangle and circle
import math
# Rect Area
length = float(input('Enter length: '))
breadth = float(input('Enter breadth: '))
rect_area = length * breadth
print(f'Area of Rectangle: {rect_area}')

# Circle Area
radius = float(input('Enter the radius: '))
circle_area = math.pi * radius ** 2
print(f'Area of Circle : {circle_area:.2f}')


# 2 - Remove Duplicate characters and vowels from a string
s = input('Enter a String: ')
vowels = 'aeiouAEIOU'
seen = []
result = ''

for ch in s:
    if ch not in vowels and ch not in seen:
        result += ch
        seen.append(ch)

print('Modified string:', result)


# 2A - Get Maxium and Minimum value in a Dictionary
d = {'a':45, 'b': 12, 'c': 78, 'd': 33}
print('Dictionary:', d)

max_val = max(d.values())
min_val = min(d.values())

print('Maxium values:', max_val)
print('Minium values:', min_val)



# SLIP 2

# 1 - Replace Special Symbols in a String with # CHaracter
import string
s = input('Enter a string: ')
special = string.punctuation   # All special Characters
result = ""

for ch in s:
    if ch in special:
        result += "#"
    
    else:
        result += ch

print('Modified String:', result)


# 2 - Find and Remove Repeated Items of a tuple
t = (1,2,3,4,4,5,5,6,6)
print('Original tuple:',t)

# Find repeated items
repeated = []
for item in t:
    if t.count(item) > 1 and item not in repeated:
        repeated.append(item)

print('Repeated items:', repeated)

# Remove Duplicated (Keep first occurrance only)
updated_tuple = tuple(set(t))
print('Removed Duplicate',updated_tuple)


# 2A - Print a Star pattern
n = int(input('enter number of rows: '))

for i in range(1, n + 1):
    print('* ' * i)



# SLIP 3 
# 1 - FIND THE LENGHT OF A TUPLE
t = (10, 20, 30, 40, 50)
print(len(t))


# 2 - MULTIPLICATION TABLE
n = int(input('Enter a number:'))
for i in range(1,11):
    print(n," X ", i, "=", n*i)


# 2A - WORDS AND STARTING INDEX
s = input("Enter Sentence:")
words=s.split()
print("Total words:",len(words))
for w in words:
    print(w,"index:", s.index(w))



# SLIP 4
# 1 - CALCULATE SUM AND AVERAGE OF NUMBERS IN A GIVEN LIST
lst = [10, 20, 30, 40, 50, 60]
total = sum(lst)
avg = total/len(lst)
print("Sum:",total)
print("Average:",avg)


# 2 - DICTIONARY WITH KEY X,Y,Z HOLDING LISTS 11-20, 21-30, 31-40 ACCESS 5th VALUE
d = {
     'x': list(range(11,21)),
     'y': list(range(21,31)),
     'z': list(range(31,41))
    }

print(d['x'][4], d['y'][4], d['z'][4])


# 2A - CHECK WHEATHER TWO STRINGS ARE EQUAL WITHOUT USING ==
s1 = input()
s2 = input()

if len(s1)!=len(s2):
    print("NOT EQUAL")
else:
    flag = True
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            flag = False
    print("Equal" if flag else "NOT EQUAL")



# SLIP 5
# 1 - CONVERT A LIST TO A TUPLE
lst = [1, 2, 3, 4]
print(tuple(lst))


# 2 - ACCEPT THREE NUMBERS AND FIND MINIMUM AND MAXIMUM
num1 = int(input('ENTER 1st NUMBER:'))
num2 = int(input('ENTER 2nd NUMBER:'))
num3 = int(input('ENTER 3rd NUMBER:'))

print(max(num1,num2,num3))
print(min(num1,num2,num3))


# 2A - COUNT UPPER AND LOWER CASE LETTER IN A STRING
s = input()
u=l=0
for ch in s:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
print("Upper:",u, "Lower:",l)



# SLIP 6
# 1 - REMOVE DUPLICATE FROM A LIST
lst = [1, 2, 4, 3 ,3, 4, 4]
print(list(set(lst)))


# 2 - COUNT UPPER CASE AND LOWER CASE LETTERS
string = input()
u = l = 0
for ch in string:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
print("Upper:",u , "Lower:", l)


# 2A - SORT A DICTIONARY BY VALUE (A-Z)
d = {
     'a':3,
     'b':1,
     'c':2
    }
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=lambda x: x[1], reverse=True))



# SLIP 7
# 1 - FIND MIXIMUM AND MINIMUM VALUES IN A SET
s = {10,20,30,40}
print(max(s),min(s))


# 2 - MASK A STRING KEEP FORST AND LAST AND REPlACE THE MIDDLE WITH *
s = input()
print(s[0] + "*" * (len(s)-2) + s[-1])


# 2A - BITWISE AND OR NOT AND XOR ON TWO NUMBERS
a = int(input("Enter a Number:"))
b = int(input("Enter another Number:"))

print('AND', a & b)
print('OR', a | b)
print('XOR', a ^ b)
print('NOT', ~a)
print('NOT', ~b)



# SLIP 8
# 1 - MERGE TWO PYTHON DICTIONARY
d1 = { 'a':1, 'b':2 }
d2 = { 'c':3, 'd':4 }

print({**d1, **d2})


# 2 - CHECK IF STRING STARTS WITH CAPITAL, ENDS WITH DIGIT, CONTAIMS SPECIAL CHARACTERS
import string
s = input('Enter a sting: ')
starts_cap = s[0].isupper() if s else False
ends_digit = s[-1].isdigit() if s else False
has_special = any(ch in string.punctuation for ch in s)

print(f'Starts with capital letter : {starts_cap}')
print(f'Ends with a digit : {ends_digit}')
print(f'Contains special character: {has_special}')

if starts_cap and ends_digit and has_special:
    print('String satisfies ALL conditions.')
else:
    print('String does NOT satisfy all conditions.')


# 2A - Accept Marks of 3 Subjects, Calculate Total, Average and Grade
sub1 = float(input('Enter Marks For Subject 1: '))
sub2 = float(input('Enter Marks For Subject 2: '))
sub3 = float(input('Enter Marks For Subject 3: '))

total = sub1 + sub2 + sub3
average = total/3

if average >= 75:
    grade = 'Distinction'
elif average >= 60:
    grade = 'First Class'
elif average >= 50:
    grade = 'Second Class'
elif average >= 35:
    grade = 'Pass'
else:
    grade = 'Fail'

print(total)
print(average)
print(grade)



# SLIP 9
# 1 - GET THE LARGEST AND SMALLEST NUMBER FROM A LIST
num = list(map(int, input().split()))
print(max(num), min(num))


# 2 - COUNT VOWELS AND CONSONANTS IN A STRING
s = input('Enter a Sentance: ')
v=c=0
for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou": v+=1
        else:c+=1
print(v,c)


# 2A - CHECK WEATHER A NUMBER IS ARMSTRONG OR NOT
n = int(input('Enter a number: '))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)

if total == n:
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is NOT an Armstrong number')



# SLIP 10
# 1 - COUNT THE NUMBER OF DIGIT IN A GIVIN NUMBER
def count_digits(n):
    return len(str(n))

print(count_digits(12345))


# 2 - CHECK WEATHER A NUMBER IS ARMSTRONG OR NOT
n = int(input('Enter a number: '))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)

if total == n:
    print(f'{n} is an Armstrong number')
else:
    print(f'{n} is NOT an Armstrong number')


# 2A - COUNT STRINGS OF LENGTH >= WHERE FIRST AND LAST CHAR ARE SAME
str_list = ['abc', 'ab', 'aba', 'hello', 'madam', 'hi', 'level']
count = 0
for s in str_list:
    if len(s) >= 3 and s[0] == s[-1]:
        count += 1
        print(f' "{s}" qualifies')

print(f'Count of qualifying strings: {count}')