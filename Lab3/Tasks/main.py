from utils import *

def main():

    startMenu()

    while True:
        enteredSymbol = input("Початкове меню \ Ввести: ")
        match enteredSymbol:
            case "1":
                groupName = enterGroup()
                createFile(groupName)
                
                groupMenu()
                while True:
                    enteredSymbol = input("Меню групи \ Ввести: ")
                    match enteredSymbol:
                        case "1":
                            readFile(groupName)
                        case "2":
                            addStudent(groupName)
                        case "3":
                            deleteStudent(groupName)
                        case "4":
                            findStudent(groupName)
                        case "0":
                            break
                        case _:
                            print("Невірний вибір. Спробуйте ще раз.")
            case "0":
                exit()
            case _:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()