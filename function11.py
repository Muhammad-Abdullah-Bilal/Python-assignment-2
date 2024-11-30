def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return (n1)

number1 = int(input("Enter first numbr:"))
number2 = int(input("Enter second numbr:"))
print(f"The greater common divisor of {number1} and {number2} is {gcd(number1, number2)}")
