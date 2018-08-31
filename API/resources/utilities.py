import string
import re


def clean_input(text):
    ''' this method cleans an input an ensures that a string was submitted '''
    # ensure that it's a string
    text = str(text)
    # specify the characters to remove
    chars = string.whitespace + string.punctuation + string.digits
    # remove the characters and return the result
    return text.strip(chars)

def check_title_length(text):
    ''' this method verifies that the title length '''
    text = str(text)
    if len(text) < 8:
        return False
    return True

def check_description_length(text):
    ''' this method verifies that the title length '''
    text = str(text)
    if len(text) < 15:
        return False
    return True

def check_answer_length(text):
    ''' this method verifies that the title length '''
    text = str(text)
    if len(text) < 10:
        return False
    return True

def check_comment_length(text):
    ''' this method verifies that the title length '''
    text = str(text)
    if len(text) < 8:
        return False
    return True

username_requirements = """
1. The username must start with an alphabet letter (a-z).
2. It can contain only alphabet letters (a-z), digits(0-9) and an underscore. 
3. It should also be between 4 to 8 characters in length.
4. It should not have any spaces in between.
"""
1. 
def validate_username(username):
    username = str(username).lower()
    if len(username.split()) > 1:
        return False
    elif re.match("^[a-z][a-z0-9_]{3,7}", username):
        return True
    return False

password_requirements = """ 
Password should have a minimum six characters, at least one letter and one number:
 """
def validate_password(password):
    if re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
        return True
    return False

def validate_email(email):
    email = str(email).lower()
    if re.match(r"^[a-z0-9\.\+_-]+@[a-z0-9\._-]+\.[a-z]*$", email):
        return True
    return False
