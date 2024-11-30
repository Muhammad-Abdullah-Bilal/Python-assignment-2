# def remove_duplicates(input_list):
#     seen = set()
#     result = []
#     for item in input_list:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# my_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = remove_duplicates(my_list)
# print("Original list:", my_list)
# print("List with duplicates removed:", unique_list)



# 2nd method 
# in this code order of list can vary
def remove_duplicates_unordered(input_list):
    return list(set(input_list))

unique_list = list(map(int, input("Enter elements separated by commas: ").split(',')))
list = remove_duplicates_unordered(unique_list)
print("List with duplicates removed (unordered):", list)
