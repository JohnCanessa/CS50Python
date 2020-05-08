# **** ****
import csv

# **** main method ****
def main():

    # **** prompt for a name and number ****
    name = input("name: ").capitalize()
    number = input("number: ")
    print(f"name: {name} number: {number}")

    # **** open the phonebook file ****
    phoneBook = "phonebook.csv"
    with open(phoneBook, "a", newline="") as file:
        
        # **** writer for csv file ****
        writer = csv.writer(file)

        # **** write the name and number to the csv file ****
        writer.writerow((name, number))

    # **** close the file ****
    # file.close()

# **** call main method ****
main()