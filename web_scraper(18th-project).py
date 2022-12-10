# we need 2 python libraries
# these libraries are requests(install process : pip install requests) &
# beautiful soup(install process: pip install bs4) .request is used for sending requests & beautiful soup is used
# for filtering the data we need specifically

import requests
from bs4 import BeautifulSoup


url = "https://twinkles-shopping-zone.netlify.app/"
r = requests.get(url)
print(r)            # it response 200 . now when it says 200 means the request was sent successfully and we've
                    # gotten a response . that means everything is okay .
                    # but we have another one or any other number it means an error


soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all('h1')
print(title)


