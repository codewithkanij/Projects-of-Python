# first of all we install schedule library .Process: type terminal-----> pip install schedule
# next we install other library which is the requests library.
# got to the website 'textbelt.com'. This is like a website they have this platform  which allows us to for
# sms marketing for various things right there but they have also api which developers can use to send text messeges
# for install request library type terminal : pip install requests then press ENTER


from credentials import mobile_number          # credentials.py file ta theke mobile number ta import korbe.
import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone': mobile_number,
        'message': 'hey,Good Morning!',
        'key': 'textbelt',
    })

    print(resp.json())


# schedule.every().day.at('06:00').do(send_message)

schedule.every(10).seconds.do(send_message)                # after every 10 seconds this message will send


while True:
    schedule.run_pending()
    time.sleep(1)



