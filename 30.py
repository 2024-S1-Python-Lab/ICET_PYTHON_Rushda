
square_area = lambda a: a**2
rectangle_area = lambda l, b: l * b
triangle_area = lambda ba, h: 0.5 * ba * h
a = int(input("Enter the side length of the square: "))
print("Area of the square:", square_area(a))
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
print("Area of the rectangle:", rectangle_area(l, b))
ba = int(input("Enter the base of the triangle: "))
h = int(input("Enter the height of the triangle: "))
print("Area of the triangle:", triangle_area(ba, h))
