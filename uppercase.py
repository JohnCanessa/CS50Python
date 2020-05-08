# **** main method ****
def main():

    # **** ****
    s = input("input: ")
    print(f"s ==>{s}<==")

    # **** convert string to uppercase one character at a time ****
    print("outout ==>", end="")
    for c in s:
        print(c.upper(), end="")
    print("<==")

    # **** convert string to uppercase build in method ****
    s = s.upper()
    print(f"output ==>{s}<==")


# **** run main method ****
main()