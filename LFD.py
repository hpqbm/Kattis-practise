
num = int(input(""))

def last_digit_factorial(n):
    # Base case
    if n == 0:
        return 1

    # Calculate the factorial of n
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    # Return the last digit of the factorial
    return fact % 10

arr = []

for i in range(1 , ( num + 1)):
    arr.append(input(""))

for number in arr:
    print(last_digit_factorial(int(number)))

