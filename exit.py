# **** ****
from sys import argv, exit


# **** main method ****
def main():

    # **** sanity check ****
    if len(argv) < 2:
        print("missing command-line argument")
        exit(1)

    # **** display list of names ****
    print("Hello", end="")
    for i in range(1, len(argv)):

        # **** skip program name ****
        # if i == 0:
        #     continue
        
        # **** display separator ****
        if i == 1:
            print(" ", end='')
        elif i == len(argv) - 1:
            print(" and ", end='')
        else:
            print(", ", end='')

        # **** display name ****
        print(f"{argv[i].capitalize()}", end='')

    # **** all done ****
    exit(0)

# **** call main method ****
main()