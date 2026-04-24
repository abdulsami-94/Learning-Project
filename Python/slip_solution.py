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



# SLIP 11
# 1 - REMOVE DUPLICATE FROM A LIST AND DISPLAY RESULTANT LIST
my_list = [1, 2, 3, 2, 4, 3, 5, 1]
print('Original List:', my_list)

unique = list(set(my_list))
print('After removing duplicate :', unique)


# 2 - ACCEPT A SENTENCE COUNT WORDS FIND LONGEST AND SHORTEST WORD
sentence = input('Enter a sentence: ')
words = sentence.split()

print(f'Number of words: {len(words)}')
longest = max(words, key=len)
shortest = min(words, key=len)

print(f'{longest} ({len(longest)} chars)')
print(f'{shortest} ({len(shortest)} chars)')


# 2 - A PRINT ALL ODD NUMBERS BETWEEN 1 AND 50 USING LOOP

i = 1

while i <= 50:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
print()
    


# SLIP 12
# 1 - Arrange String Characters so Lowercase Letters Come First
s = input('Enter a string: ')

lower_chars = [ch for ch in s if ch.islower()]
other_chars = [ch for ch in s if not ch.islower()]

result =  ''.join(lower_chars + others_chars)
print('Rearrange String:', result)


# 2 - Check if Number is Divisible by 5 and 7, and Whether its Even or Odd
n = int(input('Enter a Number : '))

if n % 5 == 0 and n % 7 == 0 :
    print(f"{n} is Divisible by 5 and 7")
elif n % 5 == 0:
    print(f"{n} is Divisible by 5")
elif n % 7 == 0:
    print(f"{n} is Divisible by 7")
else:
    print(f"{n} is Not Divisible by 5 and 7")


if n % 2 == 0:
    print("It's Even")
else:
    print("It's Odd")


# 2A - Accept a List of Integers Count Even and Odd, Separate into Two Lists
nums = list(map(int, input('Enter some Numbers: ').split()))
even_list = [ n for n in nums if n % 2 == 0 ]
odd_list = [ n for n in nums if n % 2 != 0 ]

print(even_list)
print(odd_list)



# SLIP 13 
# 1 - Swap Two Numbers
a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))

a, b = b, a

print(a , b)


# 2 - Find Words in a String that Contain Both Digits and Letters
sentence = input('Enter a Sentence: ')

words = sentence.split()
result = []

for word in words :
    has_digit = any(ch.isdigit() for ch in word)
    has_letters = any(ch.isalpha() for ch in word) 
    if has_letters and has_digit:
        result.append(word)

print('Word containing both digits and letters:', result)
    

# 2A - Remove All Occurrences of an Element from a Given List
my_list = [1, 2, 3, 2, 4, 2, 5]

elem = int(input('Enter element to remove: '))

new_list = [x for x in my_list if x != elem]
print('After removal: ', new_list)



# SPIP 14
# 1 - Interchange First and Last Element of a List
my_list = [10, 20, 30, 40]
my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)


# 2 - Find Comman Characters Between Two Strings and Check if Equal
s1 = input('Enter first string: ')
s2 = input('Enter second string: ')

common = set(s1) & set(s2)
print('Common characters :', sorted(common))


# 2A - Print the Fibonacci Sequence
n = int(input('How many terms? '))
a, b = 0, 1

print('Fibonacci Sequence: ')
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()



# SLIP 15
# 1 - Square Each Element of the List and Print in Reverse Order
my_list = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in my_list]
print('Squared List :',squared)
print('Reversed List', squared[::-1])


# 2 - Find the Sum of Natural Number
n = int(input('Enter n: '))

formula_sum = n * (n + 1) // 2
print(f'Sum of First {n} natural numbers: {formula_sum}')


# 2A - Accept a Sentence Count Words and Display in Reverse Word Order
sentence = input('Enter a sentence: ')
words = sentence.split()

print(f'Number of Words: {len(words)}')
print(f'Reversed order: {" ".join(reversed(words))}')




# SLIP 16
# 1 - Check Whether the Year is a Leap Year or Not
year = int(input('Enter a year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is NOT a Leap Year')


# 2 - Remove Duplicate Characters, Replace Spaces with UnderScore
sentence = input('Enter a Sentence: ')

seen = []
result = ''

for ch in sentence:
    if ch not in seen:
        if ch == ' ':
            result += '_'
        else:
            result += ch
        seen.append(ch)

print('Modified string:', result)


# 2A - Square Each Element and Print in Reverse Order 
my_list = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in my_list]

print('Squared :',squared)
print('Reversed Square :',squared[::-1])



# SLIP 17
# 1 - Check Whether a String is Palindrome or Not
s = input('Enter a string: '.lower())

if s == s[::-1]:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')


# 2 - Convert Decimal Number to Binary Using a Function
def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''

    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

num = int(input('Enter a decimal number: '))
print(f'Binary of {num}: {decimal_to_binary(num)}')
print(f'Built-in Check : {bin(num) [2:]}')


# 2A - Sort a Tuple
t = (2, 4, 6, 1, 4, 7.8, 2.7)

sorted_t = tuple(sorted(t))
print(sorted_t)



# SLIP 18
# 1 - Find the Maximum of Three Numbers
num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
num3 = int(input('Enter Third Number: '))

max_val = max(num1, num2, num3)
print(max_val)


# 2 - Check Whether an Element Exits Within a Tuple
value = (1, 2, 3, 4, 5, 6, 7, 8, 9)
che = int(input('Enter a Element you want to search (1-9): '))

if che in value :
    print('Element Found')
else:
    print('Not Found')


# 2A - Find the Length of a Set
s = set(map(int, input('ENter the Numbers: ').split()))

s_len = len(s)

print(s_len)
        


# SLIP 19 
# 1 - Check Whether a Number is Prime or Not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
if is_prime(n):
    print(f'{n} is PRIME')
else:
    print(f'{n} is NOT PRIME')


# 2 - Combine Two Dictionaries Adding Values for Common Keys
from collections import Counter

d1 = {'a': 100, 'b':200, 'c':300}
d2 = {'a': 300, 'b':200, 'd':400}

result = Counter(d1) + Counter(d2)
print('Combined Dictionary:', dict(result))


# 2A - Convert a TUple to a String and Display in Reverse
t = (1, 2, 3, 4, 5)

s = ''.join(str(x) for x in t)
print('As String:', s)
print('Reversed: ',s[::-1])



# SLIP 20 
# 1 - Reverse Words in a Given String
sentence = input('Enter a sentence: ')
sen_words = ' '.join(sentence.split()[::-1])
print(sen_words)


# 2 - Remove All Even Numbers from a List
li = list(map(int, input('Enter number seperate by spaces: ').split()))
odd_only = [l for l in li if l % 2 != 0]

print(li)
print(odd_only)


# 2A - Print All Prime Numbers in a Specified Range
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

start = int(input('Enter start of range: '))
end = int(input('Enter end of range : '))

primes = [n for n in range(start, end + 1) if is_prime(n)]
print(f'Prime numbers between {start} and {end}: {primes}')



# SLIP 21
# 1 - Find Minimum of Three Numbers Using a Function
def find_minimum(a, b, c):
    return min(a, b, c)

a = float(input('Enter first number : '))
b = float(input('Enter second number : '))
c = float(input('Enter third number : '))

print(f'Minimum of {a}, {b}, {c} is: {find_minimum(a, b, c)}')


# 2 - Find Symmetric Difference of Two Sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print('Set A:',A)
print('Set B:',B)

sym_diff = A ^ B 
print('Symmetric difference (A ^ B):', sym_diff)


# 2A - Find the Student with the Higest Makes from Dictionary
students = {'Alice': 85, 
            'Bob': 92, 
            'Charlia': 78, 
            'Diana': 95, 
            'Eve': 88
            }

top_students = max(students, key=students.get)
print(f'Top students: {top_students} with {students[top_students]} marks')



# SLIP 22
# 1 - Find the Factorial of a Number
def factorial(n):
    if n < 0:
        return 'Undefined (nagetive)'
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input('Enter a number: '))
print(f'{n}! = {factorial(n)}')


# SLIP 2 - Generate Dictionary of x: x*x for numbers 1 on n
n = int(input('Enter n: '))

square_dict = {x: x*x for x in range(1, n + 1)}
print(f'Dictionary (1 to {n}):',square_dict)


# SLIP 2A - Convert Lowercase to Uppercase and Vice Versa (Swap Case)
sentence = input('Enter the Words: ')
swapped = sentence.swapcase()

print('Swaped case: ',swapped)



# SLIP 23
# 1 - Get 4th Element from Front and 6th Element from Last of a Tuple
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print('Tuple:', t)

fourth_from_front = t[3]     # index 3 = 4th Element
sixth_from_last = t[-6]      # index -6 = 6th from end

print(f'4th element from front: {fourth_from_front}')
print(f'6th element from last: {sixth_from_last}')


# SLIP 2 - Function to Print Sum of All Numbers in a List
def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = list(map(int, input('Enter numbers: ').split()))
print('List:', numbers)
print('Sum :', list_sum(numbers))
print('Build-in Check: ', sum(numbers))


# 2A - Find the Factorial of a Number Using a Loop
n = int(input('Enter a number: '))

if n < 0:
    print('Factorial undifined for negative numbers')
elif n == 0 or n == 1:
    print(f'{n}! = 1')
else:
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f'{n}! = {result}')



# SLIP 24
# 1 - Split a List into Positive and Negative Number Lists
numbers = list(map(int, input('Enter numbers seperated by spaces: ').split()))
print('Input List', numbers)

positive = [n for n in numbers if n > 0]
negative = [n for n in numbers if n < 0]

print('Positive numbers:', positive)
print('Negative numbers:', negative)


# 2 - Check Whether a Number is Perfect or Not
def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

n = int(input('Enter a Number: '))
if is_perfect(n):
    print(f'{n} is a PERFECT number')
else:
    print(f'{n} is NOT a perfect number')


# 2A - Check if a Substring is Persent in a Given String
main = input('Enter the main string: ')
sub = input('Enter the substring : ')

if sub in main:
    print(f'"{sub}" IS present in "{main}"')
    print(f'Starting index: {main.index(sub)}')
else:
    print(f'"{sub}" is NOT present in "{main}"')



# SLIP 25
# 1 - Check Armstrong Number
n = int(input('Enter a number:'))
digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)

if total == n:
    print(f'{n} is an Armstrong Number')
else:
    print(f'{n} is NOT an Armstrong number')


# 2 - Accept n Elements -- Find Largest, Smallest, Sum, and Average
n = int(input('How many elemnts? '))
numbers = []
for i in range(n):
    numbers.append(float(input(f'Enter element {i + 1}: ')))

print(f'List : {numbers}')
print(f'Largest : {max(numbers)}')
print(f'Smallest : {min(numbers)}')
print(f'Sum : {sum(numbers)}')
print(f'average : {sum(numbers)/len(numbers):.2f}')


#2A - Create a Dictionary from a String (Character Frequency)
s = input('Enter a string: ').lower()
freq = {}

for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

print('Character frequency dictionary:', freq)



# SLIP 26
# 1 - Sum All items in a List
my_list = list(map(int, input('Enter numbers: ').split()))
print('List:', my_list)

print('Sum :',sum(my_list))


# 2 - Function to Check if a Number is a Given Range
def in_range(n, low, high):
    return low <= n <= high

n = float(input('Enter a number :'))
low = float(input('Enter lower bound :'))
high = float(input('Enter upper bond :'))

if in_range(n ,low, high):
    print(f'{n} IS in the range [{low}, {high}]')
else:
    print(f'{n} is NOT in the range [{low}, {high}]')


# 2A - Create a List of Tuples (Numbers, Square of Number)
n = int(input('Enter how many numbers: '))

result = [(x, x**2) for x in range(1, n + 1)]
print('List of (number, square) tuples:')
for items in result:
    print(f' {items}')



# SLIP 27
# 1 - Check if a Number is Odd or Even
n = int(input('Enter a Number: '))    
if n % 2 == 0:
    print(f'{n} is Even')
else:
    print(f'{n} is Odd')


# 2 - Count Upper Case and Lower Case Letters in a String
def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

s = input('Enter a string: ')
u, l = count_case(s)
print(f'Upper case letters: {u}')
print(f'Lower case letters: {l}')


# 2A - Partition a List: Negatives First, Then Zeros, Then Positives
numbers = list(map(int, input('Enter integers: ').split()))
print('Input list:', numbers)

negatives = [n for n in numbers if n < 0]
zeros = [n for n in numbers if n == 0]
positives = [n for n in numbers if n > 0]

result = negative + zeros + positive
print(result)



# SLIP 28 
# 1- Perform Arithmetic Operations (+, -, *, /, %)
a = float(input('Enter first number : '))
b = float(input('Enter second number : '))

print(f'Addition : {a} + {b} = {a + b}')
print(f'Subtraction : {a} - {b} = {a - b}')
print(f'Multiplication : {a} * {b} = {a * b}')

if b != 0:
    print(f'Division : {a} / {b} = {a / b:.2f}')
    print(f'Modulus : {a} % {b} = {a % b}')
else:
    print('Division/Modulus: undefined (division by zero)')


# 2 - Create Union and Intersection of Two Sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
print('Set A:', A)
print('Set B:', B)

union = A | B
intersection = A & B

print('Union (A | B):', union)
print('Intersection (A & B):', intersection)


# 2A - Concatenate Three Dictionaries into One New Dictionary
dic1 = {1: 11, 2: 22}
dic2 = {3: 33, 4: 44}
dic3 = {5: 55, 6: 66}

merged = {**dic1, **dic2, **dic3}
print('Merged dictionary:', merged)

merged2 = {}
for d in [dic1, dic2, dic3]:
    merged2.update(d)
print('Merged (update) :', merged2)



# SLIP 29
# 1 - Check if a Number is Positive, Negative, or Zero
n = float(input('Enter a number: '))

if n > 0:
    print(f'{n} is Positive')
elif n < 0:
    print(f'{n} is Negative')
else:
    print(f'{n} is Zero')


# 2 - Copy Elements 22 and 66 from tuple1 into a New Tuple
tuple1 = (11, 22, 33, 44, 55, 66)
print('Original tuple:', tuple1)

new_tuple = (tuple1[1], tuple[5])
print('New tuple (22 and 66):', new_tuple)


# 2A - Convert Lowercase to Uppercase and Vise Versa
s = input('Enter a string: ')

swapped = s.swapcase()
print('Swapped case (build-in):', swapped)


# SLIP 30
# 1 - Find the Frequnecy of Characters in a String
s = input('Enter a String: ')
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print('Character frequncires:')
for char, count in sorted(freq.items()):print(f' "{char}": {count}')


# 2 - Count items in a Dictionary Without Uning len()
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print('Dictionary:, d')

count = 0
for _ in d:
    count += 1

print(f'Number of items (without len()): {count}')


# 2A - Function to Check Whether a Number is Prime (Retuen True/False)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
result = is_prime(n)
print(f'{n} is prime: {result}')