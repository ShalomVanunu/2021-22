lst1 = [85,60,40,50,100,90,40]

for score in lst1 :
    if score <80:
        indx = lst1.index(score)
        lst1[indx]= score+5
print(lst1)

dict = {"shalom":23,"Hila":17}

print(dict["Hila"])
list_names = []
for key in dict.keys():
    list_names.append(key)
print(list_names)
print(list_names[1])