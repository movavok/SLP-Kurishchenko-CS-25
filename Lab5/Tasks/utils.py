from classCoffeeShop import CoffeeShop
from classHomeLibrary import HomeLibrary

def chooseClass():
    """
    Main function to choose between Coffee Shop and Home Library functionalities.
    Returns: None
    """
    coffee_shop = CoffeeShop()
    home_library = HomeLibrary()
    
    while True:
        print("\nChoose a programm to work with.")
        print("1 -> Coffee shop")
        print("2 -> Home library")
        print("0 -> Exit")
        match input("Enter your choice: "):
            case "1": coffee_shop.show_menu()
            case "2": home_library.show_menu()
            case "0": return
            case _: print("Invalid choice. Please try again.")