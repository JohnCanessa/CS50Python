# **** to use regular expressions ****
import re

# **** prompt for and get response ****
# s = input("Do you agree? ").upper()
s = input("Do you agree? ")
print(f"s ==>{s}<==\n")

# **** ****
if s[0].upper() == 'Y':
    print("Agreed.")
elif s[0].upper() == 'N':
    print("Not agreed.")
else:
    print("What do you mean?")

# **** ****
if s[0] in ['y']:
    print("Agreed.")
elif s[0] in ['n']:
    print("Not agreed.")
else:
    print("What do you mean?")

# **** with regular expressions ****
if re.search("^y(es)?$", s, re.IGNORECASE):
    print("Agreed.")
elif re.search("^n(o)?$", s, re.IGNORECASE):
    print("Not agreed.")
else:
    print("What do you mean?")
