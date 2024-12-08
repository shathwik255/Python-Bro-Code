# collection = single "variable" used to store multiple values
#   List = [] order and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LISTS
# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[0])
# print(fruits[0:3])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("apple" in fruits)
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits.index("apple")
# fruits.index("pineapple")
# print(fruits.count("banana"))
# print(fruits)


# SETS
# fruits = {"apple", "orange", "banana", "coconut"}
# for fruit in fruits:
#     print(fruit)
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(dir(fruits))
print(fruits.index("apple"))
print(fruits.count("coconut"))
for fruit in fruits:
    print(fruit)
