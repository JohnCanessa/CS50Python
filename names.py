# **** ****
from sys import exit

# **** main method ****
def main():

    # **** list of names ****
    names = ["emma", "Rodrigo", "brian", "JOHN", "david", "james"]
    print(f"names: {names}\n")
    
    # **** prompt for name ****
    name = input("name to search in list: ")

    # **** check if we are done ****
    if name == "":
        exit(0)

    # **** search for the specified name in the list (ignore spelling) ****
    # found = False
    # for n in names:
    #     if (name.capitalize() == n.capitalize()):
    #         found = True
    #         print(f"found {name} in list")
    #         break

    # # **** ****
    # if not found:
    #     print(f"{name} NOT in list :o(")
    #     exit(-1)
    # else:
    #     exit(0)

    # **** search for the specified name in the list (must match spelling)****
    if name in names:
        print(f"found {name} in list :o)")
        exit(0)
    else:
        print(f"{name} NOT in list :o(")
        exit(-1)

# **** call main method ****
main()