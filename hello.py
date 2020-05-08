# **** print string ****
print("hello, world !!!")

# **** prompt for name and print it ****
name = input("What is your name? ")
print("Hello,", name, "!!!")
print("Hello. " + name + " !!!")
print(f"Hello, {name} !!!")
print()

# **** initialize and increment counter ****
counter = 0
print(f"counter: {counter}")
counter = counter + 1
print(f"counter: {counter}")
counter += 1
print(f"counter: {counter}")
print()

# **** compare integers ****
x = 8
y = 7
if x < y:
    print(f"x: {x} < y: {y}")
elif x == y:
    print(f"x: {x} == y: {y}")
else:
    print(f"x: {x} > y: {y}")
print()

# **** loop forever but exit loop at break ****
while True:
    print("hello, world !!!")
    break
print()

# **** loop until condition is met ****
i = 0
while i < 3:
    print(f"cough i: {i}")
    i += 1
print()

# **** loop for each element in the list ****
for i in [1, 2, 3]:
    print(f"cough i: {i}")
print()

# **** loop for each element in the list ****
for i in ['potato', 'carrot', 'letuce']:
    print(f"cough i: {i}")
print()

# **** loop for the specified range ****
for i in range(3):
    print(f"cough i: {i}")
print()