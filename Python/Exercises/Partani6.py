
while True:
    input_temp = input("Insert the temparature you would like to convert [exit] :") #50.5F 30C
    if input_temp == "exit":
        break
    temp = float(input_temp[:-1]) #original -  50.7
    c_or_f = input_temp[-1].upper() #C.c.F.F --> c f
    if c_or_f == 'C':
        F = (9*temp+(32*5)/5)
        print(f"{F}F")
        print(str(F)+"F")
    elif c_or_f == "F":
        C = (5*temp-160)/9
        print(f"{C}C")
