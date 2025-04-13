import os
import csv

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
    groupNames = {
                        "КН-24": "KN-24.csv",
                        "КБ-24": "KB-24.csv",
                    }

    groupKey = input("Введіть назву групи: ")
    if groupKey in groupNames: 
        return groupNames[groupKey]
    else:
        print("Групи з такою назвою не існує. Є такі групи: КН-24, КБ-24.")
        return enterGroup()

def createFile(fileName):
    """
    Створити файл, якщо він не існує, і заповнити його даними.
    """
    if not os.path.exists(fileName):
        with open(fileName, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["№", "Прізвище", "Ім'я", "Середній бал"])

    