from modules import menu
from modules import manager

from os import system, name

def clearscr():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

if __name__ == "__main__":
    clearscr()

    while True:
        try:
            menu.showMainMenu()
            c = input("Choose an option: ")
            if c == "1":
                clearscr()
                manager.showAccounts()
            if c == "2":
                clearscr()
                manager.modifyAccount()
            if c == "3":
                clearscr()
                manager.addAccount()
            if c == '4':
                clearscr()
                print(f"Generated password: {manager.generatePassword()}")
            if c == '5':
                clearscr()
                print("Goodbye")
                exit()
            input("Press enter to continue...")
            clearscr()
        except KeyboardInterrupt:
            clearscr()
            print("Goodbye!")
            exit()

