import math

m = float(input("Enter a whole number > 3: "))

if m <= 3:
    print("The number you entered is not greater than 3.")
else:
    z = float(math.sqrt((m + 3) / (m - 3)))
    print("The result 'z' is: ", z)

