
### Patrik`s functions

def add():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a + b
    print(a, "+", b, "=", res)

def subtract():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a - b
    print(a, "-", b, "=", res)

def multiply():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    res = a * b
    print(a, "*", b, "=", res)

def divide():
    a = float(input("\nEnter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("You enetred zero ! Try one more time without zero )")
        divide()
    else:
        res = a / b 
        print(a, "/", b, "=", res)

### Jurek Functions 

def power():
    a = float(input("\nPodaj podstawe: "))
    b = float(input("Podaj wyk�adnik: "))
    wyn = a ** b
    print(a, "^", b, "=", wyn)

def factorial():
    a = int(input("\nPodaj liczbe do silni: "))
    if a in (0,1):
        wyn=1
    else:	    
        wyn=1 
        for i in range(2, a+1):
            wyn *= i
    print(a, "! =", wyn)
