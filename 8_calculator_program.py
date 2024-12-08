# Python calculator
operator = input("Enter the operator (+ - * /): ")
num_1 = float(input("Enter the 1st number: "))
num_2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num_1 + num_2
    print(round(result, 3))
elif operator == "-":
    result = num_1 - num_2
    print(round(result, 3))
elif operator == "*":
    result = num_1 * num_2
    print(round(result, 3))
elif operator == "/":
    result = num_1 / num_2
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator")
