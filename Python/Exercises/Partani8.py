
dict_math = {"Alon":88,"Itizk":77, "Tom":66}


# add more 4 puples+scores to the dictionary
for x in range(4):
    name =  input("enter name: ")
    number = int(input("enter score: "))
    dict_math[name] = number

print(dict_math)



print(dict_math.keys())
for name in dict_math.keys():
    print(name)

print(dict_math.values())