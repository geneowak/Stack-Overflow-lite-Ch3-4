import string


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