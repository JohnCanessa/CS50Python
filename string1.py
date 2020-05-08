
# **** main method ****
def main():

    # **** prompt and display string ****
    s = input("input: ")
    print(f"s ==>{s}<==")

    # **** display the string character by character ****
    print("output ==>", end="")
    for i in range(len(s)):
        print(s[i], end="")
    print("<==")

    # **** a more pythonic approach ****
    print("output ==>", end="")
    for c in s:
        print(c, end="")
    print("<==")

# **** call main method ****
main()
