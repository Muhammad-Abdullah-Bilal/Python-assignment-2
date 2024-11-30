def factorial_cal(n):
    if n == 0:  
        return 1
    elif n < 0:  
        return "The factorial of a negative number does not exist"
    else:
        return n * factorial_cal(n - 1)  

number = int(input("Enter your number:"))
print("The factorial of a given number is:", factorial_cal(number))

# Second method
# def factorial_cal(n):
#     if n == 0:
#       return 1
#     elif n < 0:
#       return "The factorial of negative number does not exist"
#     else:
#       factorial = 1
#       while n >= 1:
#         factorial = factorial * n
#         n = n-1
#     return factorial    
    
# number = int(input("Enter your number:"))
# print("The factorial of a given number is:", factorial_cal(number))
