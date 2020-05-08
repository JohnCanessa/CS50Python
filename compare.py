# **** ****
from sys import exit

# **** main method ****
def main():

    # **** prompt for two strings ****
    s = input("string s: ")
    print(f"s ==>{s}<==")

    t = input("string t: ")
    print(f"t ==>{t}<==")

    # **** compare strings ****
    if s == t:
        print(f"s: {s} equals t: {t}")
        exit(0)
    print(f"s: {s} NOT equal to t: {t}")
    exit(-1)

# **** call main ****
main()