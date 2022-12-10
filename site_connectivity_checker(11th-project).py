# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url
# returns a response

import urllib.request as urllib


def main(url):
    print("Checking connectivity  ")

    response = urllib.urlopen(url)
    print("Connected to ",url,"successfully")
    print("The response code was: ",response.getcode())   # ekhane '200' ashe kno ???


print("This is a site connectivity program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)                    # ekhane bracket er vitor sudhu 'url' na hoye 'input_url' kno hoiche???
