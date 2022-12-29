# install library Pillow if you haven't  (it's better to say that this library ave default here.so it
#  doesn't need to install)
# import image
# open up the image we want to resize using python
# resize kora picture ta folder a save hoye jabe


from PIL import Image

image = Image.open('cute-cartoon-girl.jpg')

print(f"Current size : {image.size}")


def resize_image(size1, size2):
    resized_image = image.resize((size1,size2))                       # resize er command
    resized_image.save("cute-cartoon-girl" + str(size1) + ".jpeg")    # resize kora picture save howar jonno


size1 = int(input("Enter Width : "))
size2 = int(input("Enter Length : "))

resize_image(size1,size2)                                           # ficntion call

print("resized successfully")                                       # program a sob clear thakle eta print korbe
