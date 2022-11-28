def print_menu():
    print("\n1) NOK & NOD \n2) IMT\n")

def exit_menu():
    print("\nEnter 99 for exit :)")   
    exit = int(input("Do you want to exit: "))
    if exit == 99:
        repeat_menu()

def repeat_menu ():
    print_menu()
    print("If you want to exit the programm enter 99: ")
    choose_menu = int(input("Select menu number: "))
    if choose_menu == 1:
        first_menu()
    elif choose_menu == 2:
        second_menu()
    elif choose_menu == 99:
        exit

def first_menu():
    a = int(input("\nEnter first argument (a): "))
    b = int(input("Enter second argument (b): "))
    def NOD(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        print(f"\nYour NOD is: {a}")
        return a

    res = a * b / NOD(a, b) 
    print(f"Your NOK is: {res}")
    exit_menu()
    
def second_menu():
    heigt = int(input("Enter your height: "))
    weight = int(input("Enter your weight: "))
    result = weight/(heigt*2)
    print(f"\nYour MBI is: {result}")
    exit_menu()
        
if __name__ == "__main__":
    print_menu()
    choose_menu = int(input("Select menu number: "))
    if choose_menu == 1:
        first_menu()
    elif choose_menu == 2:
        second_menu()


