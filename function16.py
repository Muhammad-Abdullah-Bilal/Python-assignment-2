def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if sorted(str1) == sorted(str2):
        return(f"{str1} and {str2} are anagrams.")
    else:
        return(f"{str1} and {str2} are not anagrams.")
     

string1 = input("Enter the first string:")
string2 = input("Enter the second string:")
result = are_anagrams(string1, string2)
print(result)