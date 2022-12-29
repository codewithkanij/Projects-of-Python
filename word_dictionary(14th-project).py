# first of all install pydictionary.process:if you are on Mac type "pip3 intall PyDictioary" then press ENTER
# if you are on Windows type "pip install PyDictionary" then press ENTER


from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break

    print(dictionary.meaning(word))



#                                                     OR                                                          .



"""



from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes","indentation","head")

print(dictionary.printMeanings())          # instead of 'printMeanings()' we just want to say 'getMeanings()'

                                           # python dictionary format a dekhabe 

"""