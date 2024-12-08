# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exists")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "New York"})
# capitals.pop("China")
# capitals.clear()

# keys = capitals.keys()
# for key in keys:
#     print(key)

# values = capitals.values()
# for value in values:
#     print(value)

items = capitals.items()

for key, value in items:
    print(f"{key}: {value}")
