def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temp_in_celcius = int(input("Enter temperature in celsius:"))
result1 = celsius_to_fahrenheit(temp_in_celcius)
print(temp_in_celcius, "°C is equal to ", result1, "°F")

temp_in_fahrenheit = int(input("Enter temperature in fahrenheit:"))
result2 = fahrenheit_to_celsius(temp_in_fahrenheit)
print(temp_in_fahrenheit, "°F is equal to", result2, "°C")
