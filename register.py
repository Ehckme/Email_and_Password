# import the re (regex module)
import re
"""
The following methods checks both the email and validates the 
passwords to match
"""

def check_email():
    while True:
        # Ask email from user to register
        register_email = input("enter email: ").strip()
        # set a regex input sequence to match input email
        if re.match(r"\S[^@]+\S+@[^@]+\S+[a-zA-Z]+\S+\.[^@]", register_email):
            print("Okay")
        else:
            print("invalid  email")


check_email()


def validate_password():
    while True:
        # Ask for password input from user
        register_password = input("enter password: ").strip()
        # Check if password field is empty and notify user with an if statement
        if register_password == " " or register_password == "":
            print("Password field cannot be empty. ")
        # Make sure that the password is not less than eight characters
        elif len(register_password) < 8:
            print("Password should contain a minimum of 8 characters. ")
        else:
            user_password = register_password
            while True:
                confirm_password = input("Confirm password: ").strip()
                if confirm_password != register_password:
                    print("password do not match: ")
                else:
                    user_password = register_password
                    print("Passwords match. ")
                    break
                validate_password()
                break
            break
    print(user_password)
    return user_password


validate_password()
