import os

file_name = input("enter the file name to search ?: ")

os.chdir("c:\\")
list_dir = os.listdir()
for dir in list_dir:
    try:
        if "." not in dir:
            os.chdir(dir)
        #print(os.getcwd())
            if os.path.isfile(file_name):
                print(f"the file is found in path-->{dir} ")
            os.chdir("c:\\")
    except:
        pass






