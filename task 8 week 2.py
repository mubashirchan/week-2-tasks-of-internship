#Temperature Converter
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = (fahrenheit_input - 32) * 5/9
    print(f"{fahrenheit_input}°F = {celsius_result:.2f}°C")

except ValueError:
    print("Invalid input! Please enter a number.")