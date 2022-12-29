# string concatenation (how to put string together)
# suppose we want to create a string that says "subscribe to _____"
# youtuber ="Kylin Ying"
# some string variable
"""
# a few ways to do this

youtuber = input()
print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")
"""
adj = input("Adjective: ")
verb1 = input("Verb1 : ")
verb2 = input("Verb2 : ")
famous_person = input("Famous person : ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because " \
 f"I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"


print(madlib)
