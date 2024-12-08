# name = input("Enter your full mane: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("o")
# result = name.rfind("q")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", "")

# print(result)
# print(help(str))

# Valid user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
username = input("Enter the username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") != -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}")
