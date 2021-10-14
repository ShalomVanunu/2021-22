
#this program generate Password
import string
import random

ABC = string.ascii_uppercase
abc = string.ascii_lowercase
sign = string.punctuation


while True:
    password = ""
    password_len = int(input("Enter Pass len [>4]"))
    if password_len < 4:
        continue
    password += random.choice(ABC)
    for x in range(password_len-2):
        password += random.choice(abc)
    password += random.choice(sign)
    print(password)



