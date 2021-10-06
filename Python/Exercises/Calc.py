# this program calc two numbers

print(" this program calc two numbers")
while True:
    math_arg= input(" choose your math arg [+,-,*,/ E for Exit] :")
    if math_arg == "e" or math_arg =="E":
        break
    num1 = float(input("enter number 1 :"))
    num2 = float(input("enter number 2 :"))

    if math_arg == '+':
        print(f" the result num1 {math_arg} num2 is : {num1+num2}")
    elif math_arg == '-':
        print(f" the result num1 {math_arg} num2 is : {num1 - num2}")
    elif math_arg == '*':
        print(f" the result num1 {math_arg} num2 is : {num1 * num2}")
    elif math_arg == '/':
        print(f" the result num1 {math_arg} num2 is : {num1 / num2}")