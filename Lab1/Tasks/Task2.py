n = int(input("Enter an integer > 0: "))
y = int(1)

if n <= 0:
    print("The number you entered is not greater than 0.")
else:
    for i in range(2, 2*n + 1, 2):
        y = int(i * y)

print("The result 'y' is: ", y)