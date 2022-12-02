import calculator

### Menu 

def print_menu():
    print("\n1) Sum \n2) Subtract\n3) Multiply\n4) Divide\n")

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
    elif choose_menu == 99:
        exit

### Calculator functions menu 

def first_menu():
    calculator.add()
    exit_menu()
    
def second_menu():
    calculator.subtract()
    exit_menu()

def third_menu():
    calculator.multiply()
    exit_menu()

def fourth_menu():
    calculator.divide()
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


