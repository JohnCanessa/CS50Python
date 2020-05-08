# **** swap method ****
def swap(x, y):
    y, x = x, y
    return x, y


# **** main method ****
def main():

    # **** define two variables ****
    x = 1
    y = 2
    print(f"[0] x: {x} y: {y}\n")

    # **** swap variables in-line ****
    temp = x
    x = y
    y = temp
    print(f"[1] x: {x} y: {y}\n")

    # **** swap variables (for free with Python) ****
    y, x = x, y
    print(f"[2] x: {x} y: {y}\n")

    # **** swap variables (overkill using a method) ****
    x, y = swap(x, y)
    print(f"[3] x: {x} y: {y}\n")


# **** call main method ****
main()