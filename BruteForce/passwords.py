
# my methods

def get_password():
    file_content = open("Passwords.txt", "r")
    list_of_password = file_content.readlines()
    return list_of_password