import random

def create_array(n):
    if n <= 0:
        print("The number you entered is not greater than 0.")
        exit()

    array = [random.randint(-100, 100) for i in range(n)]
    print("The array is: ", array)
    return array

def first_task(array): #Find the max negative number in the array
    max_negative = None
    for i in array:
        if i < 0 and (max_negative is None or i > max_negative):
            max_negative = i
    if max_negative is None:
        print("There are no negative numbers in the array.")
    else:
        print("The max negative number is: ", max_negative)

def second_task(array): #Calculate the arithmetic mean of paired elements in the array
    sum = 0
    count = 0

    for i in range(0, len(array), 2): 
        sum += array[i]
        count += 1
    print("The count of paired elements in the array is: ", count)
    print("The arithmetic mean of paired elements in the array is: ", sum / count)

def third_task(array): #Move all elements except the first one in reverse order
    array[1:] = array[1:][::-1]
    print("The array with all elements except the first one in reverse order is: ", array)

def main():
    n = int(input("Enter a count of numbers in the array: "))
    array = create_array(n)
    first_task(array)
    second_task(array)
    third_task(array)

main()