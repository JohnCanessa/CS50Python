# **** ****
from sys import argv

# **** main method *****
def main():

    # **** display program arguments ****
    for i in range(len(argv)):
        print(f"argv[{i}]: {argv[i]}")
    print()

    # **** display program arguments (more pythonic way) ****
    for arg in argv:
        print(arg)

# **** call main method ****
main()