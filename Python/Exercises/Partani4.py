# "Insert the Tempreture you would like to to convert [exit] : 50F,50f
# 10C
while True:
    insert = input("Insert the Tempreture you would like to to convert [exit]")
    if insert == "exit":
        break
    sign = insert[-1].upper() #string
    number = float(insert[:-1]) # for x in range(10) 0-9 ||for x in range(3,9) 3-8
    #c,C,f,F
    if sign == "C":
        F = ((9*number+32*5)/5) #float
        print(str(F)+"F")
        print(f"{F}F")
    elif sign == "F":
        C = ((5*number-160)/9)
        print(f"{C}C")




