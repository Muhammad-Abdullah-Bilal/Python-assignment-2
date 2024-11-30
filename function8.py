def nth_fibonacci_number(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        n1, n2 = 0, 1
        for i in range(2, n):
            nth = n1 + n2
            n1, n2 = n2, nth
        return nth

number = int(input("Enter any number:"))
result = nth_fibonacci_number(number)
print(f"The Fibonacci number at position {number} is: {result}")