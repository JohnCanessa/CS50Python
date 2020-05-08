# **** prompt for x and y ****
x = int(input("x: "))
y = int(input("y: "))

# **** compare x and y ****
if x < y:
    print(f"x: {x} < y: {y}")
elif x == y:
    print(f"x: {x} == y: {y}")
else:
    print(f"x: {x} > y: {y}")