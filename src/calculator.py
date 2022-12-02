def add_():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a + b
    print(a, "+", b, "=", res)

def subtract_():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a - b
    print(a, "-", b, "=", res)

def multiply_():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a * b
    print(a, "*", b, "=", res)

def divide_():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("You enetred zero ! Try one more time without zero )")
        divide()
    else:
        res = a / b 
        print(a, "/", b, "=", res)