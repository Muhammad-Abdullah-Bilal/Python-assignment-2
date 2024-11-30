def cal_power(num, pow):
    if pow < 0:
        num = 1 / num  
        pow = -pow 
    answer = 1
    for i in range(pow):
      answer *= num
    return answer 

number = int(input("Enter number whose power is to calculate:"))
power = int(input("Enter the power to find the power of a number:"))
result = cal_power(number, power)
print("The answer after finding the power of a given number is:", result)
 