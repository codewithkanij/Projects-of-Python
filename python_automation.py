# first of all we install schedule library .Process: type terminal-----> pip install schedule
# next we install other library which is the requests library.
# got to the website 'textbelt.com'. This is like a website they have this platform  which allows us to for
# sms marketing for various things right there but they have also api which developers can use to send text messeges
# for install request library type terminal : pip install requests then press ENTER

from credentials import mobile_number
import requests
def send_message():
    resp = requests.post('https://textbelt.com/text',{      # this is a text belt website which was sending or posting our data
        'phone': mobile_number,
        'message':'hey,Good Morning!',
        'key':'textbelt'
    })

    print(resp.json())


print('sent message successfully')


