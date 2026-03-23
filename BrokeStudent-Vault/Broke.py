print("Hello World")

# Indentation Rules
# The Golden Rule
# CORRECT — 4 spaces each level
if True:
    print("level 1")      # 4 spaces
    if True:
        print("level 2")  # 8 spaces



#Data Types
# Integers - whole numbers
age = 25
score = -10
big = 1_000_000    # underscores for readability — totally valid

print(type(age))   # <class 'int'>
print(10 // 3)      # 3  ← floor division (drops remainder)
print(10 % 3)       # 1  ← modulo (remainder only)
print(2 ** 8)       # 256 ← exponentiation



# Floats - decimal number
price = 9.99
pi = 3.14159

print(0.1 + 0.2)   # 0.30000000000000004 ← welcome to floating point

# Convert between int and float:
print(int(9.9))    # 9   ← truncates, does NOT round
print(float(5))    # 5.0



# Complex numbers with imaginary parts
z = 3 + 4j
print(z.real)    # 3.0
print(z.imag)    # 4.0
print(abs(z))     # 5.0  ← magnitude



# String -text
name = "Alice"
greeting = 'Hello'

# f-strings — the modern way to embed variables
print(f"{greeting}, {name}!")   # Hello, Alice!

# Common string operations
print(name.upper())           # ALICE
print(name.lower())           # alice
print(len(name))              # 5
print(name[0])               # A  ← indexing starts at 0
print(name[-1])              # e  ← last character
print(name[1:3])             # li ← slicing

# Concatenation
print("Hello" + " World")    # Hello World
print("ha" * 3)               # hahaha



# Booleans 
is_raining = True
is_sunny = False

# Comparison operators produce booleans
print(5 > 3)      # True
print(5 == 5)     # True  ← == not =
print(5 != 3)     # True
print(5 >= 10)    # False

# Logical operators
print(True and False)  # False
print(True or False)   # True
print(not True)         # False

# "Truthy" and "Falsy" — Python treats these as False:
# 0, 0.0, "", None, [], {}
print(bool(0))    # False
print(bool(""))   # False
print(bool(42))   # True



# Control Flow
score = 72

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# While Loops
count = 0 
while count < 5:
    print(f"count is {count}")
    count +=1 

# break exit loop immediately
n = 0 
while True:
    if n == 3:
        break
    n +=1

# for loops
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop a specific number of times with range()
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step=2)
    print(i)

# continue — skip current iteration, carry on
for i in range(5):
    if i == 2:
        continue   # skip when i is 2
    print(i)
# Output: 0 1 3 4  (2 is missing)


# FizzBuzz — the classic example
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
