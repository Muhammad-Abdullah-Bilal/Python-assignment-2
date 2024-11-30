def count_vowels(string):
    count = 0
    vowels = "AEIOUaeiou"  
    for char in string:
        if char in vowels:
            count += 1
    return count  

vowel_count = count_vowels("Hello everyone my name is Muhammad Abdullah Bilal")
print("The number of vowels in the given string is:", vowel_count)
