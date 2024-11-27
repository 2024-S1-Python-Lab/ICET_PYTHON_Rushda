def swap(a,b):
    return b,a
a=int(input("enter a:"))
b=int(input("enter b:"))
a,b=swap(a,b)
print(f"after swapping: a = {a}, b = {b}")
