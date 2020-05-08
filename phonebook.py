# **** ****
from sys import exit

# **** main method ****
def main():

    # **** dictionary (associative array) ****
    people = {
        "EMMA" : "617-555-0100",
        "RODRIGO" : "617-555-0101",
        "BRIAN" : "617-555-0102",
        "DAVID" : "617-555-0103",

        "JAMES" : "617-007-0071",
        "JOHN" : "617-007-0072"
    }
    print(f"people: {people}\n")

    # **** prompt for a name ****
    name = input("name: ").upper()
    print(f"looking for name: {name.capitalize()}")

    # **** search for the name in people ****
    if name in people:
        print(f"found: {name.capitalize()} phone: {people[name.upper()]}")

        phone = people.get(name)
        print(f"found: {name.capitalize()} phone: {phone}")

        # **** done ****
        exit(0)
    
    # **** name not found ****
    print(f"name: {name.capitalize()} NOT found")
    exit(-1)

# **** call main method ****
main()
