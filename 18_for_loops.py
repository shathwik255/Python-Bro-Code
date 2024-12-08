# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for x in reversed(range(1, 11)):
#     print(x)
# print("HAPPY NEW YEAR!")

# for x in (range(1, 11, 2)):
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue  # Works for WHILE loop also
#     print(x)

for x in range(1, 21):
    if x == 13:  # Works for WHILE loop also
        break
    print(x)
