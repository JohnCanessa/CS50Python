
# **** prompt user and loop until positive number is entered ****
def get_positive_int():

    # **** loop until condition is satisfied ****
    while True:

        # **** prompt user ****
        n = int(input("positive integer: "))

        # **** check if done ****
        if n > 0:
            break;
    
    # **** return positive integer ****
    return n


# **** main method ****
def main():

    # **** prompt for and return a positive integer ****
    i = get_positive_int()
    print(f"i: {i}")


# **** call main method ****
main()
