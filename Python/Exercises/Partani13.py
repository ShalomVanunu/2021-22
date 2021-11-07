
file_read = open("names.txt", "r")
content = file_read.read()
print(content)

#_________________________

file = open(r"C:\Users\shalomvanunu\Desktop\names.txt", "w") #file object
# w -write
# r- read
# a - append (add)

for times in range(3):
    name = input("Enter a name :")
    file.write(name+",") #\n - new line



