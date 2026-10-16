def factorial(a):
    total = 1
    while a != 0:
        total *= a
        a -= 1
    print("Factorial is:", total)
num = int(input("Enter a number: "))
factorial(num)

