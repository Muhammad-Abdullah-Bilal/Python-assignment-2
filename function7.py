def largest_number(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
result = largest_number(numbers)
print("The largest number from the given list is:", result)
