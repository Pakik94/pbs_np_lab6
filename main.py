from src import calculator as calc

### Menu 

def print_menu():
    print("\n1) Sum \n2) Subtract\n3) Multiply\n4) Divide\n5) Power\n6) Factorial\n")

def exit_menu():  
    exit = int(input("\nIf you want to exit, enter 99: "))
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
    elif choose_menu == 3:
        third_menu()
    elif choose_menu == 4:
        fourth_menu()
    elif choose_menu == 5:
        fifth_menu()
    elif choose_menu == 6:
        sixth_menu()
    elif choose_menu == 99:
        exit

### Calculator functions menu 

def first_menu():
    calc.add()
    exit_menu()
    
def second_menu():
    calc.subtract()
    exit_menu()

def third_menu():
    calc.multiply()
    exit_menu()

def fourth_menu():
    calc.divide()
    exit_menu()

def fifth_menu():
    calc.power()
    exit_menu()

def sixth_menu():
    calc.factorial()
    exit_menu()

### Start script func         

if __name__ == "__main__":
    print_menu()
    choose_menu = int(input("Select menu number: "))
    if choose_menu == 1:
        first_menu()
    elif choose_menu == 2:
        second_menu()
    elif choose_menu == 3:
        third_menu()
    elif choose_menu == 4:
        fourth_menu() 
    elif choose_menu == 5:
        fifth_menu()
    elif choose_menu == 6: 
        sixth_menu()


