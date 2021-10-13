
names = ["Jessy","Hila","Liel","Lihi","Zohar"]

print(names)
print(len(names))
names.append("Noa")
print(names)

for name in names:
    print(name)

asked_name = input("enter your name :")
if asked_name in names:
    print(f" the name {asked_name}is on the list")