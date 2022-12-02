def power():
    a = float(input("\nPodaj podstawe: "))
    b = float(input("Podaj wyk³adnik: "))
    wyn = a ** b
    print(a, "^", b, "=", wyn)

def factorial():
    a = float(input("\nPodaj liczbe do silni: "))
    if a in (0,1):
        wyn=1
    else:
	    wyn=1 
        for i in range(2,a+1):
            wyn *= i
    print(a, "! =", wyn)
