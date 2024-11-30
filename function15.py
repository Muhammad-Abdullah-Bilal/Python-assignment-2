# def flatten_list(nested_list):
#     flattened = []
#     for item in nested_list:
#         if isinstance(item, list):
#             flattened.extend(flatten_list(item))
#         else:
#             # Add the item if it's not a list
#             flattened.append(item)
#     return flattened

# nested_list = [1, [2, 3], [4, [5, 6]], 7]
# result = flatten_list(nested_list)
# print("Flattened list:", result)




# second method
def flatten_once(nested_list):
    return [item for sublist in nested_list for item in sublist]
    
nested_list = [[1, 2], [3, 4], [5, 6]]
result = flatten_once(nested_list)
print("Flattened list:", result)
