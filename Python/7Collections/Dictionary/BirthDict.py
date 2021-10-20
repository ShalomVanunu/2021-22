
name_birth = {"Noa":"21/3/2005","Roni":"1/7/2005","Jessy":"30/9/2005"}


for name in name_birth.keys():
    print(name)

for name in name_birth.keys(): #"Noa", Rone Jessy
    print(name_birth[name])

for birth in name_birth.values():
    print(birth)