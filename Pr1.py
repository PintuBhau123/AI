# Factorial Program
num = int(input("Enter a number for factorial: "))
fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is:", fact)


# Fibonacci Program
n = int(input("\nEnter number of terms for Fibonacci series: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nJayant75")