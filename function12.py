def key_with_highest_value(my_dict):
    return max(my_dict, key=my_dict.get)

user_dict = {pair.split('=')[0]: int(pair.split('=')[1]) for pair in input("Enter the dictionary (key=value) pairs separated by spaces: ").split()}
result = max(user_dict, key=user_dict.get) if user_dict else None
print(f"The key with the highest value is: {result}")
