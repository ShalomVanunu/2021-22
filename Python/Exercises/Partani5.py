
#dict = {key:value}
dict = {"Moshe": "12/12/1987","itzik":"3/4/2005"}

for x in range(3): # 0,1,2
    name = input("enter Name")
    birth = input("enter Birthday")
    dict[name] = birth
#dict["Meriam"]= "12/4/2005"

print(dict.keys())
print(dict.values())
print(dict["Moshe"])
for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)



num2 = 6
num ="name"
print(f"the number you guess is :",num, "and", num2)

print(f"the number you guess is :{num} and {num2}")