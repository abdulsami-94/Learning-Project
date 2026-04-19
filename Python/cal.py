# Asking user for the numbers
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

print(num1 , num2)

# Asking the Operator to perform action
print("Choose the operator:")
print("1. Addition +")
print("2. Subtraction -")
print("3. Multiplication *")
print("4. Division /")
print("5. Modulo %")
print("6. Square **")
print("7. Factorial n!")
print("8. Fibonacci sequence")

operator = input()

def add(num1, num2):
    result = num1 + num2
    print(f"The answer is {result}")
    return result

def sub(num1, num2):
    result = num1 - num2
    print(f"The answer is {result}")
    return result

def  mul(num1, num2):
    result = num1 * num2
    print(f"The answer is {result}")
    return result

def div(num1, num2):
    if num2 == 0:
        print("Can't divide by zero.")
        return
    result = num1 / num2
    print(f"The answer is {result}")
    return result

def modulo(num1, num2):
    result = num1 % num2
    print(f"The answer is {result}")
    return result

def square(num1, num2):
    result = num1 ** num2
    print(f"The answer is {result}")
    return result

def factorial(num1, num2):

    if num1 < 0:
        print("Factorial is not defined for negative numbers.")
        return None

    fact = 1
    for i in range(1, num1 + 1):
        fact = fact * i
    result = fact
    print(f"The answer is {result}")
    return result

def fibonacci(num1, num2):
    if num1 < 0:
        print("Fibonacci is not defined for negative numbers.")
        return None

    a = 0
    b = 1

    for i in range(num1):
        c = a + b
        a = b
        b = c

    result = a
    print(f"The answer is {result}")
    return result

operations = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div,
    '5': modulo,
    '6': square,
    '7': factorial,
    '8': fibonacci,
}

func = operations.get(operator)
if func:
    func(num1, num2)
else:
    print("Choose the correct operator.")


