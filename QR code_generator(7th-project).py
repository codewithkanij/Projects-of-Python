# install all the libraries needed (open new terminal, then write - pip install qrcode Image , then press  ENTER)
# create a function that collect a text and converts it to a QRcode
# save the QR as an image
# run the function

import qrcode


def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,

    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimg.png")


generate_qrcode("https://www.codewithkanij.com")

