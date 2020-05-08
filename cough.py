# **** cough 3 times ****
print("cough")
print("cough")
print("cough")
print()

# **** cough 3 times ****
print("cough\n" * 3)

# **** cough 3 times ****
for i in range(3):
    print("cough")
print()

# **** define cough method ****
def cough(n):
    for i in range(n):
        print("cough")

# **** cough 3 times ****
# for i in range(3):
#    cough()
cough(3)
print()

# **** define main method ****
def main():
    # for i in range(3):
    #     cough()
    cough(3)

# **** call main method ****
main()