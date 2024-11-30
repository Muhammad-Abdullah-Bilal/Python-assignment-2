def prime_check(num):
    if num <= 1:
        return "The given number is not prime"
    for i in range(2, num):
        if num % i == 0:
            return "The given number is not prime"
    return "The given number is prime"

number = int(input("Enter any number:"))
print(prime_check(number))
