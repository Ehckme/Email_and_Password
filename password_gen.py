import random
import string

"""
The following method expresses and defines random
password generator.
It uses standard non Alpha-Numeric password compatable characters.

It is good for generating random Password for users. 
"""
def random_chars(random_chars_length):
    punc = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "<", ">", "?"]
    string_punc = "".join(punc)
    password_chars = "".join(random.choice(string.ascii_lowercase + string_punc + string.hexdigits)
                             for i in range(random_chars_length))
    return password_chars


password_gen = random_chars(16)
print(password_gen)