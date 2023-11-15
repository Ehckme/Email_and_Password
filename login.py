# import the re (regex module)
import re
"""
The following method checks for valid email input
from the user.
It can be modified and customised according to needs
specification.
"""

def check_email():
    while True:
        # Ask user input for email
        login_email = input("enter email: ").strip()
        # set a regex input sequence
        if re.match(r"\S[^@]+\S+@[^@]+\S+[a-zA-Z]+\S+\.[^@]", login_email):
            print("Okay")
        else:
            print("invalid  email")


check_email()
