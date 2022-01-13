
import os

# cat /etc/passwd
# os.system

users_list = os.popen("cat /etc/passwd").readlines()
#print(users_list)

for user in users_list:
        print(user.split(":")[0])

#print(users_list[0].split(":"))

