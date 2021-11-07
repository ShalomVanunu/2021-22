
dict_pass = {}

for num in range(3):
    site = input(" Enter site :")
    password = input(" Enter Site Password")
    dict_pass[site]= password

pass_file = open("sitepasswords.txt","a") #w

for key in dict_pass.keys():
    pass_file.write(key+" :"+dict_pass[key])
    pass_file.write("\n") #new line
