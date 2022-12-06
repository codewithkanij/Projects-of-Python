# Collect email from user
# split the email using the @ ,the first  part as the user name, the second part is gonna be saved as domain
# split domain using. ,
# ( Hello@codewithkanij.com )
def email_slicer():
    print(" Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("username: ",username)
    print("domain: ",domain)
    print("extension: ",extension)

while True:
    email_slicer()


