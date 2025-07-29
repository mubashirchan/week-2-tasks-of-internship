# Data Type Tester
user_input = input("Enter any value: ")

try:
    val = int(user_input)
    print("You entered an integer!")
except:
    try:
        val = float(user_input)
        print("You entered a float!")
    except:
        print("You entered a string!")