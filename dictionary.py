# default dictionary from:
# https://www.mit.edu/~ecprice/wordlist.10000


# **** set of words (this is our dictionary) ****
words = set()


# **** check if this word is in the dictionary ****
def check(word):
    if word.lower() in words:
        return True
    else:
        return False


# **** read from specified file the contents for the dictionary (in lowercase) ****
def load(dictionary):

    # **** open dictionary ****
    file = open(dictionary, "r")

    # **** read the dictionary and populate the set of words ****
    for line in file:
        words.add(line.strip().lower())

    # **** close dictionary ****
    file.close()

    # **** indicate all is well ****
    return True


# **** get the number of words in the dictionary ****
def size():
    return len(words)


# **** free words in dictionary ****
def unload():
    words = set()
    return True


# **** main method ****
def main():

    # **** get the name for the dictionary ****
    dictionary = input("dictionary (blank to load default): ")

    # **** dictionary not specified (use default one) ****
    if dictionary == "":
        dictionary = "dict.txt"
    print(f"dictionary ==>{dictionary}<==")

    # **** load the dictionary ****
    if not load(dictionary):
        print(f"load dictionary: {dictionary} failed !!!")
        exit(-1)

    # **** get the number of words in the dictionary ****
    count = size()
    print(f"dictionary has {count} words")

    # **** loop looking up words in the dictionary ****
    while True:
        
        # **** prompt for word to check ****
        word = input("word (blank to exit): ")

        # **** check if we are done (exit loop) ****
        if word == "":
            break

        # **** check the word ****
        if check(word):
            print(f"found word: {word}")
        else:
            print(f"word: {word} NOT found !!!")

    # **** unload the dictionary ****
    if not unload():
        print(f"unload dictionary: {dictionary} failed !!!")
        exit(-1)


# **** call main method ****
main()