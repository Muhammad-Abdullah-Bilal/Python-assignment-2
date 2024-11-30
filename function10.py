def list_of_integers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
          even_sum += num
    return even_sum
    
result = list_of_integers([2, 4, 5, 7, 8, 9])
print("The sum of all the even numbers in a given list is:", result)
