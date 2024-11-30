def check_palindrome(str):
    if str == str[::-1]:
        return "The given string is a palindrome"
    return "The given string is not a palindrome"

string = input("Enrer a string to check if it is a palindrome or not:")
print(check_palindrome(string))