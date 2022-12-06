# have a python dictionary that has a key/value pair that represents a word and it's defination
# collect input from the user,input is a word
# check if the word is in the dictionary
# print the defination

def main():
    word_dictionary = {
        'hi' : 'a way of greeting',
        'eyes' : 'an organ for seeing',
        'earth' : 'a planet in space',

    }

    while True:
        search = input("Enter a word: ")

        if search == "":     # once i enter nothing and i click enter it breaks out of that program
            break
        if search in word_dictionary:
            print(search, ":",word_dictionary[search])


main()