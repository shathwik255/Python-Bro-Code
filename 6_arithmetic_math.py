import math

friends = 10
# friends = friends - 2
# friends = friends + 2
# friends = friends * 2
# friends = friends ** 2
# friends = friends / 2
# friends = friends // 2
# friends = friends % 2
friends -= 2
friends += 2
friends *= 2
friends **= 2
friends /= 2
friends //= 2
friends %= 2
# print(friends)

x, y, z = 3.14, -4, 5
result = round(x)
result = abs(y)
result = pow(z, y)
result = max(x, y, z)
result = min(x, y, z)

# Math module
print(math.pi)
print(math.e)
result = math.sqrt(z)
result = math.ceil(9.1)
result = math.floor(9.9)
print(result)

# Circumference of a circle
radius = float(input("Enter the radius of a circle(cm): "))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

# Area of circle
radius = float(input("Enter the radius of the circle(cm): "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 2)}")

# Hypotenuse of a triangle
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print(f"Side C is {side_c}")
