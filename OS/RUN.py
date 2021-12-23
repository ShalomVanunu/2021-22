import os

#run the program
os.system("notepad")

#run the cmd and get the result
cmd = os.popen("whoami").read()
print(cmd)

os.mkdir(cmd.replace("\\","-")[:-1])