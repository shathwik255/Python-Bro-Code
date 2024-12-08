# function = A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
# happy_birthday("John", 30)
# happy_birthday("Tom", 14)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Joe", 100.99, "01/07")

# return = statement used to end a function
#          and send a result back to the caller

def add(num1, num2):
    return num1 + num2


result = add(3, 4)
print(result)
