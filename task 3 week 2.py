# Data Types
text = "Hello"       # string
number = 10          # integer
decimal = 3.14       # float
flag = True          # boolean
complex_num = 2 + 3j # complex

variables = [text, number, decimal, flag, complex_num]

for var in variables:
    print(f"Value: {var}, Type: {type(var)}")

# Converting types (where possible)
print("\nAfter conversion:")
print(str(number))       # int to string
print(int(decimal))      # float to int
print(float(number))     # int to float
print(int(flag))         # bool to int
# Complex can't be converted easily to int/float