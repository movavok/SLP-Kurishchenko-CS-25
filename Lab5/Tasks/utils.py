from classCoffeeShop import CoffeeShop

def mainMenu():
    print("\nChoose a programm to work with.")
    print("1 -> Coffee shop")
    print("2 -> Home library")
    print("0 -> Exit")

def chooseClass():
    coffee_shop = CoffeeShop()
    
    while True:
        mainMenu()
        match input("Enter your choice: "):
            case "1": coffee_shop.show_menu()
            case "2": print("You chose Home library.")
            case "0": return
            case _: print("Invalid choice. Please try again.")