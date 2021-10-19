
pedion = []
sum = 0

for day in range(7):
    pedion_day = float(input("Enter Pedion for today :"))
    pedion.append(pedion_day)
    sum += pedion_day

print(pedion)

print("Day Min Pedion",pedion.index(sorted(pedion)[0])+1)
print("Day Max Pedion",pedion.index(sorted(pedion)[-1])+1)

pedion.sort()
print(pedion)
print("Min value :",pedion[0])
print("Max Value :",pedion[-1])
#print(pedion)
#print(sum)
