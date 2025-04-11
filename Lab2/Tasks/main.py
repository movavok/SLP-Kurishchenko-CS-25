from utils import squareParams, isNumberPrime, randomList, listOfBiggerNumbers, amountOfSameNumbers, listOfRepeatedNumbers, listOfUniqueElements

def main():

    # first function
    print("Area: {0}, Perimeter: {1}, Diagonal: {2}".format(*squareParams(float(input("Enter the length of the side of the square: ")))))
    
    # second function
    print("Is your number prime?", 
        isNumberPrime(int(input("Enter a number between 0 and 1000: "))))

    # third function
    print("Your random list:", 
        randomList(int(input("Enter the number of elements in the list: "))))

    # fourth function
    print("All numbers in your list that bigger than your number:", 
      listOfBiggerNumbers(
          int(input("Enter a number: ")), 
          list(map(int, input("Enter the numbers in the list (space-separated): ").split()))
      ))

    # fifth function
    print("Amount of same numbers in your list:", 
       amountOfSameNumbers(
           int(input("Enter a number: ")), 
           list(map(int, input("Enter the numbers in the list (space-separated): ").split()))
       ))

    # sixth function
    print("New list with all elements that repeat:",
          listOfRepeatedNumbers(
              list(map(int, input("Enter the numbers in the first list (space-separated): ").split())),
              list(map(int, input("Enter the numbers in the second list (space-separated): ").split()))
          ))

    # seventh function
    print("New list with all elements of the first list that don't appear in the second list:",
          listOfUniqueElements(
              list(map(int, input("Enter the numbers in the first list (space-separated): ").split())),
              list(map(int, input("Enter the numbers in the second list (space-separated): ").split()))
          ))

if __name__ == "__main__":
    main()
