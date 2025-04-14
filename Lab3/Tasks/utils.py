import os
import csv

groupNames = {
    "КН-24": "KN-24.csv",
    "КБ-24": "KB-24.csv"
}

studentsKN = [
    [1,"Куріщенко", "Павло", 99.0],
    [2,"Мельник", "Дмитро", 97.0],
    [3,"Мироненко", "Ярослав", 96.0],
    [4,"Булюкін", "Володимир", 94.0],
    [5,"Червонець", "Артем", 92.0]
]
studentsKB = [
    [1,"Зарицький", "Віктор", 98.0],
    [2,"Колесник", "Віктор", 97.0],
    [3,"Кондратенко", "Дмитро", 94.0],
    [4,"Олефіров", "Гліб", 93.0],
    [5,"Павешенко", "Степан", 91.0]
]

def startMenu():
    """
    Відобразити початкове меню.
    """
    print("*Програма для роботи з групами студентів*")
    print("(Введіть: '1') -> Вибір групи студентів для роботи з нею")
    print("(Введіть: '0') -> Вихід з програми\n")

def groupMenu():
    """
    Відобразити меню групи.
    """
    print("(Введіть: '1') -> Вивести інформацію про студентів")
    print("(Введіть: '2') -> Додати студента до групи")
    print("(Введіть: '3') -> Видалити студента з групи")
    print("(Введіть: '4') -> Знайти студента за його прізвищем")
    print("(Введіть: '0') -> Повернення до початкового меню")

def enterGroup():
    """
    Ввести назву групи.
    """
    groupKey = input("Введіть назву групи: ")
    if groupKey in groupNames: 
        return groupNames[groupKey]
    else:
        print("Групи з такою назвою не існує. Є такі групи: КН-24, КБ-24.")
        return enterGroup()
    
def whatGroup(fileName):
    """
    Визначити, з якою групою працювати.
    """
    if fileName == "KN-24.csv": students = studentsKN
    else: students = studentsKB
    return students

def sortedStudents(students):
    """
    Відсортувати студентів за середнім балом.
    """
    students.sort(key=lambda x: float(x[3]), reverse=True)
    for i, student in enumerate(students, start=1): student[0] = i 

def createFile(fileName):
    """
    Створити файл, якщо він не існує, і заповнити його даними.
    """
    if not os.path.exists(fileName):
        with open(fileName, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["№", "Прізвище", "Ім'я", "Середній бал"])
            students = whatGroup(fileName)
            sortedStudents(students)
            writer.writerows(students)
        print(f"Файл '{fileName}' створено.")
    else:
        print(f"Файл '{fileName}' вже існує.")

def showInfo(fileName):
    """
    Вивести інформацію про студентів.
    """
    sortedStudents(whatGroup(fileName))
    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<3} {:<15} {:<15} {}".format(*row))

def addStudent(fileName):
    """
    Додати студента до групи.
    """
    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        students = list(reader)

    if len(students) > 1:
        lastRow = int(students[-1][0])
    else:
        lastRow = 0

    number = lastRow + 1
    surname = input("Введіть прізвище студента: ").strip()
    name = input("Введіть ім'я студента: ").strip()
    score = float(input("Введіть середній бал студента: "))
    if not surname: return print("Прізвище не може бути порожнім.")
    if not name: return print("Ім'я не може бути порожнім.")
    if score < 0 or score > 100: return print("Середній бал повинен бути в межах від 0 до 100.")

    students.append([number, surname, name, score])

    header = students[0]  
    students = students[1:]  
    sortedStudents(students)

    for i, student in enumerate(students, start=1):
        student[0] = i
    students.insert(0, header)

    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print(f"Студента {surname} {name} додано до групи з оцінкою {score}.")

def deleteStudent(fileName):
    """
    Видалити студента з групи.
    """
    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        students = list(reader)

    surname = input("Введіть прізвище студента для видалення: ").strip()
    if not surname: return print("Прізвище не може бути порожнім.")
    
    found = False
    for i in range(1, len(students)):
        if students[i][1] == surname:
            found = True
            del students[i]
            break

    if not found: return print(f"Студента з прізвищем {surname} не знайдено.")

    header = students[0]  
    students = students[1:]  
    sortedStudents(students)

    for i, student in enumerate(students, start=1):
        student[0] = i
    students.insert(0, header)

    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print(f"Студента {surname} видалено з групи.")

def findStudent(fileName):
    """
    Знайти студента за його прізвищем.
    """
    with open(fileName, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        students = list(reader)

    surname = input("Введіть прізвище студента для пошуку: ").strip()
    if not surname: return print("Прізвище не може бути порожнім.")
    
    found = False
    for student in students[1:]:
        if student[1] == surname:
            found = True
            print("{:<3} {:<15} {:<15} {}".format("№", "Прізвище", "Ім'я", "Середній бал"))
            print("{:<3} {:<15} {:<15} {}".format(*student))
            break

    if not found:
        print(f"Студента з прізвищем {surname} не знайдено.")

def groupLoop(fileName):
    """
    Цикл для роботи з групою.
    """
    enteredSymbol = input("Меню групи \\ Ввести: ")
    match enteredSymbol:
        case "1":
            showInfo(fileName)
        case "2":
            addStudent(fileName)
        case "3":
            deleteStudent(fileName)
        case "4":
            findStudent(fileName)
        case "0":
            return
        case _:
            print("Невірний вибір. Спробуйте ще раз.")
    return groupLoop(fileName)

def mainLoop():
    """
    Головний цикл програми.
    """
    startMenu()
    enteredSymbol = input("Початкове меню \\ Ввести: ")
    match enteredSymbol:
        case "1":
            fileName = enterGroup() 
            createFile(fileName)
            groupMenu()
            groupLoop(fileName)
        case "0":
            exit()
        case _:
            print("Невірний вибір. Спробуйте ще раз.")
    return mainLoop()

